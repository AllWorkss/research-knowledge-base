/* ==========================================================================
   ZenithAlgo Pro - Core Logic, Chart Engine & Interactive Backtester
   ========================================================================== */

// Global State
const state = {
    symbol: 'NIFTY',
    timeframe: '5m',
    indicators: {
        ema: true,
        supertrend: true,
        vwap: true,
        bb: false,
        rsi: true,
        signals: true
    },
    candles: [],
    activeBroker: 'Upstox API v2',
    tradeHistory: []
};

// Dynamic API Base URL helper (supports Localhost and Cloud Deployment e.g., GCP)
function getApiBaseUrl() {
    const host = window.location.hostname || 'localhost';
    const protocol = window.location.protocol.startsWith('http') ? window.location.protocol : 'http:';
    return `${protocol}//${host}:5000`;
}

// Base Stock Data Seeds
const stockSeeds = {
    NIFTY: { basePrice: 24340, volatility: 25 },
    BANKNIFTY: { basePrice: 52180, volatility: 60 },
    RELIANCE: { basePrice: 2980, volatility: 8 },
    TCS: { basePrice: 4210, volatility: 12 },
    TATAMOTORS: { basePrice: 1040, volatility: 5 },
    HDFCBANK: { basePrice: 1650, volatility: 6 }
};

// Initialize Application
document.addEventListener('DOMContentLoaded', () => {
    generateCandleData();
    calculateRisk();
    initEquityChart();
    startLiveTickSimulation();
    initMobileDrawer();
});

// Tab Switcher
function switchTab(tabId) {
    closeMobileSidebar();

    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));

    const targetTab = document.getElementById(tabId);
    if (targetTab) targetTab.classList.add('active');

    const navBtn = document.querySelector(`.nav-btn[data-tab="${tabId}"]`);
    if (navBtn) navBtn.classList.add('active');

    // Re-render chart canvas if chart studio is active
    if (tabId === 'chart-studio') {
        setTimeout(() => {
            renderMainChart();
            renderRsiChart();
        }, 50);
    }
}

// Indicator Toggles
function toggleIndicator(indKey) {
    state.indicators[indKey] = !state.indicators[indKey];
    const btn = document.getElementById(`btn-${indKey}`);
    if (btn) btn.classList.toggle('active', state.indicators[indKey]);
    renderMainChart();
    if (indKey === 'rsi') {
        document.getElementById('rsi-container').style.display = state.indicators.rsi ? 'flex' : 'none';
    }
}

function setTimeframe(tf) {
    state.timeframe = tf;
    document.querySelectorAll('.tf-btn').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
    generateCandleData();
}

function updateChartData() {
    state.symbol = document.getElementById('symbol-select').value;
    document.getElementById('chart-symbol-name').innerText = `${state.symbol} Index (${state.timeframe.toUpperCase()} Intraday)`;
    generateCandleData();
}

// ==================== CANDLESTICK GENERATOR & INDICATOR MATH ====================
function generateCandleData() {
    fetch(`${getApiBaseUrl()}/api/market_data?symbol=${state.symbol}`)
        .then(response => {
            if (!response.ok) throw new Error('API Error');
            return response.json();
        })
        .then(data => {
            if (data.status === 'success' && data.candles) {
                state.candles = data.candles.map(c => ({
                    ...c,
                    time: new Date(c.time)
                }));
            } else {
                throw new Error('No candles');
            }
            finishCandleSetup();
        })
        .catch(e => {
            console.warn("Using fallback random data due to API error: ", e);
            const seed = stockSeeds[state.symbol] || stockSeeds.NIFTY;
            let price = seed.basePrice;
            const count = 45;
            state.candles = [];

            let now = new Date();
            now.setHours(9, 15, 0, 0);

            for (let i = 0; i < count; i++) {
                const change = (Math.random() - 0.48) * seed.volatility;
                const open = price;
                const close = open + change;
                const high = Math.max(open, close) + Math.random() * (seed.volatility * 0.4);
                const low = Math.min(open, close) - Math.random() * (seed.volatility * 0.4);

                price = close;
                state.candles.push({
                    time: new Date(now.getTime() + i * 5 * 60000),
                    open, high, low, close,
                    volume: Math.floor(Math.random() * 5000) + 1000
                });
            }
            finishCandleSetup();
        });
}

function finishCandleSetup() {
    // Calculate Indicators
    calculateEMAs();
    calculateVWAP();
    calculateSupertrend();
    calculateRSI();
    calculateBollingerBands();
    generateSignals();
    
    // Re-render
    renderMainChart();
    renderRsiChart();
}

function calculateEMAs() {
    let ema9 = state.candles[0].close;
    let ema21 = state.candles[0].close;
    const k9 = 2 / (9 + 1);
    const k21 = 2 / (21 + 1);

    state.candles.forEach((c, idx) => {
        if (idx === 0) {
            c.ema9 = c.close;
            c.ema21 = c.close;
        } else {
            ema9 = (c.close * k9) + (ema9 * (1 - k9));
            ema21 = (c.close * k21) + (ema21 * (1 - k21));
            c.ema9 = ema9;
            c.ema21 = ema21;
        }
    });
}

function calculateVWAP() {
    let cumVol = 0;
    let cumTPV = 0;
    state.candles.forEach(c => {
        const tp = (c.high + c.low + c.close) / 3;
        cumTPV += tp * c.volume;
        cumVol += c.volume;
        c.vwap = cumTPV / cumVol;
    });
}

function calculateSupertrend() {
    state.candles.forEach((c, idx) => {
        const factor = 1.2;
        if (c.close > c.open) {
            c.supertrend = c.low - (c.high - c.low) * factor;
            c.stDir = 'UP';
        } else {
            c.supertrend = c.high + (c.high - c.low) * factor;
            c.stDir = 'DOWN';
        }
    });
}

function calculateRSI() {
    let gains = 0, losses = 0;
    const period = 14;

    for (let i = 0; i < state.candles.length; i++) {
        if (i === 0) {
            state.candles[i].rsi = 50;
            continue;
        }
        const diff = state.candles[i].close - state.candles[i - 1].close;
        if (diff >= 0) gains += diff;
        else losses -= diff;

        if (i < period) {
            state.candles[i].rsi = 50;
        } else {
            const avgGain = gains / period;
            const avgLoss = losses / period;
            const rs = avgLoss === 0 ? 100 : avgGain / avgLoss;
            state.candles[i].rsi = 100 - (100 / (1 + rs));
        }
    }

    const latestRsi = state.candles[state.candles.length - 1].rsi.toFixed(2);
    document.getElementById('rsi-value-text').innerText = `RSI: ${latestRsi}`;
}

function calculateBollingerBands() {
    const period = 20;
    state.candles.forEach((c, idx) => {
        if (idx < period) {
            c.bbUpper = c.high;
            c.bbLower = c.low;
            c.bbMid = c.close;
        } else {
            const slice = state.candles.slice(idx - period, idx);
            const mean = slice.reduce((acc, curr) => acc + curr.close, 0) / period;
            const stdDev = Math.sqrt(slice.reduce((acc, curr) => acc + Math.pow(curr.close - mean, 2), 0) / period);
            c.bbMid = mean;
            c.bbUpper = mean + (2 * stdDev);
            c.bbLower = mean - (2 * stdDev);
        }
    });
}

function generateSignals() {
    state.candles.forEach((c, idx) => {
        if (idx > 5 && c.ema9 > c.ema21 && state.candles[idx - 1].ema9 <= state.candles[idx - 1].ema21 && c.rsi > 48) {
            c.signal = 'BUY';
        } else if (idx > 5 && c.ema9 < c.ema21 && state.candles[idx - 1].ema9 >= state.candles[idx - 1].ema21) {
            c.signal = 'SELL';
        } else {
            c.signal = null;
        }
    });

    const lastCandle = state.candles[state.candles.length - 1];
    document.getElementById('sig-entry').innerText = `₹${lastCandle.close.toFixed(2)}`;
    document.getElementById('sig-sl').innerText = `₹${(lastCandle.close - 50).toFixed(2)} (-50 pts)`;
    document.getElementById('sig-tp').innerText = `₹${(lastCandle.close + 100).toFixed(2)} (+100 pts)`;
}

// ==================== HTML5 CANVAS CHART DRAWING ====================
function renderMainChart() {
    const canvas = document.getElementById('mainChartCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;
    ctx.scale(dpr, dpr);

    const width = rect.width;
    const height = rect.height;

    // Background & Grid
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, width, height);

    ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
    ctx.lineWidth = 1;
    for (let y = 0; y < height; y += 40) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(width, y);
        ctx.stroke();
    }

    const padding = { top: 20, bottom: 30, left: 10, right: 60 };
    const chartW = width - padding.left - padding.right;
    const chartH = height - padding.top - padding.bottom;

    const prices = state.candles.flatMap(c => [c.high, c.low]);
    const minP = Math.min(...prices) * 0.998;
    const maxP = Math.max(...prices) * 1.002;

    const getY = (p) => padding.top + chartH - ((p - minP) / (maxP - minP)) * chartH;
    const candleWidth = chartW / state.candles.length;

    // Draw Price Labels Right Axis
    ctx.fillStyle = '#9ca3af';
    ctx.font = '10px JetBrains Mono';
    ctx.textAlign = 'left';
    for (let i = 0; i <= 5; i++) {
        const p = minP + (i / 5) * (maxP - minP);
        const y = getY(p);
        ctx.fillText(`₹${p.toFixed(1)}`, width - 55, y + 3);
    }

    // 1. Draw Bollinger Bands Area
    if (state.indicators.bb) {
        ctx.fillStyle = 'rgba(59, 130, 246, 0.06)';
        ctx.beginPath();
        state.candles.forEach((c, idx) => {
            const x = padding.left + idx * candleWidth + candleWidth / 2;
            if (idx === 0) ctx.moveTo(x, getY(c.bbUpper));
            else ctx.lineTo(x, getY(c.bbUpper));
        });
        for (let idx = state.candles.length - 1; idx >= 0; idx--) {
            const c = state.candles[idx];
            const x = padding.left + idx * candleWidth + candleWidth / 2;
            ctx.lineTo(x, getY(c.bbLower));
        }
        ctx.closePath();
        ctx.fill();
    }

    // 2. Draw Candlesticks
    state.candles.forEach((c, idx) => {
        const x = padding.left + idx * candleWidth + candleWidth / 2;
        const isGreen = c.close >= c.open;

        ctx.strokeStyle = isGreen ? '#10b981' : '#ef4444';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(x, getY(c.high));
        ctx.lineTo(x, getY(c.low));
        ctx.stroke();

        ctx.fillStyle = isGreen ? '#10b981' : '#ef4444';
        const bodyY = getY(Math.max(c.open, c.close));
        const bodyH = Math.max(2, Math.abs(getY(c.open) - getY(c.close)));
        const bw = Math.max(2, candleWidth * 0.7);
        ctx.fillRect(x - bw / 2, bodyY, bw, bodyH);

        // Signal Markers
        if (state.indicators.signals && c.signal) {
            ctx.fillStyle = c.signal === 'BUY' ? '#10b981' : '#ef4444';
            ctx.font = 'bold 12px Outfit';
            ctx.textAlign = 'center';
            const sigY = c.signal === 'BUY' ? getY(c.low) + 16 : getY(c.high) - 8;
            ctx.fillText(c.signal === 'BUY' ? '▲ BUY' : '▼ SELL', x, sigY);
        }
    });

    // 3. Draw EMA Lines
    if (state.indicators.ema) {
        drawLine(ctx, state.candles, 'ema9', '#3b82f6', 2, getY, padding, candleWidth);
        drawLine(ctx, state.candles, 'ema21', '#8b5cf6', 2, getY, padding, candleWidth);
    }

    // 4. Draw VWAP Line
    if (state.indicators.vwap) {
        drawLine(ctx, state.candles, 'vwap', '#f59e0b', 2, getY, padding, candleWidth, true);
    }

    // Update OHLC Readout
    const last = state.candles[state.candles.length - 1];
    document.getElementById('ohlc-readout').innerText = 
        `O: ₹${last.open.toFixed(2)} | H: ₹${last.high.toFixed(2)} | L: ₹${last.low.toFixed(2)} | C: ₹${last.close.toFixed(2)}`;
}

function drawLine(ctx, candles, key, color, width, getY, padding, candleWidth, dash = false) {
    ctx.strokeStyle = color;
    ctx.lineWidth = width;
    if (dash) ctx.setLineDash([4, 4]);
    else ctx.setLineDash([]);
    ctx.beginPath();
    candles.forEach((c, idx) => {
        const x = padding.left + idx * candleWidth + candleWidth / 2;
        const y = getY(c[key]);
        if (idx === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
    });
    ctx.stroke();
    ctx.setLineDash([]);
}

function renderRsiChart() {
    if (!state.indicators.rsi) return;
    const canvas = document.getElementById('rsiCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;
    ctx.scale(dpr, dpr);

    const w = rect.width;
    const h = rect.height;

    ctx.fillStyle = '#0b0f19';
    ctx.fillRect(0, 0, w, h);

    const getY = (val) => h - (val / 100) * h;
    const candleWidth = w / state.candles.length;

    // Overbought 70 & Oversold 30 Lines
    ctx.strokeStyle = 'rgba(239, 68, 68, 0.4)';
    ctx.setLineDash([2, 2]);
    ctx.beginPath(); ctx.moveTo(0, getY(70)); ctx.lineTo(w, getY(70)); ctx.stroke();

    ctx.strokeStyle = 'rgba(16, 185, 129, 0.4)';
    ctx.beginPath(); ctx.moveTo(0, getY(30)); ctx.lineTo(w, getY(30)); ctx.stroke();
    ctx.setLineDash([]);

    // Draw RSI Curve
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 2;
    ctx.beginPath();
    state.candles.forEach((c, idx) => {
        const x = idx * candleWidth + candleWidth / 2;
        const y = getY(c.rsi);
        if (idx === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
    });
    ctx.stroke();
}

// ==================== RISK CALCULATOR LOGIC ====================
function calculateRisk() {
    const capital = parseFloat(document.getElementById('calc-account').value) || 500000;
    const riskPct = parseFloat(document.getElementById('calc-risk-pct').value) || 1.5;
    const entry = parseFloat(document.getElementById('calc-entry').value) || 24340;
    const sl = parseFloat(document.getElementById('calc-sl').value) || 24290;
    const target = parseFloat(document.getElementById('calc-target').value) || 24440;

    const maxLoss = (capital * riskPct) / 100;
    const slPoints = Math.abs(entry - sl);
    const targetPoints = Math.abs(target - entry);

    const qty = slPoints > 0 ? Math.floor(maxLoss / slPoints) : 0;
    const lots = Math.floor(qty / 50);
    const expectedProfit = qty * targetPoints;
    const rrRatio = slPoints > 0 ? (targetPoints / slPoints).toFixed(1) : 0;

    document.getElementById('res-max-loss').innerText = `₹${maxLoss.toLocaleString('en-IN')}`;
    document.getElementById('res-sl-points').innerText = `${slPoints.toFixed(2)} Pts`;
    document.getElementById('res-qty').innerText = `${qty} Shares`;
    document.getElementById('res-lots').innerText = `(${lots} NIFTY Lots of 50)`;
    document.getElementById('res-expected-profit').innerText = `₹${expectedProfit.toLocaleString('en-IN')}`;
    document.getElementById('res-rr').innerText = `1 : ${rrRatio}`;
}

// ==================== REAL BACKTESTER ENGINE ====================
function runBacktest() {
    if (!state.candles || state.candles.length < 10) {
        showToast('Insufficient candle data to run backtest.', 'danger');
        return;
    }

    const stratName = document.getElementById('bt-strategy').value;
    const selectedSymbol = document.getElementById('bt-symbol').value;
    
    showToast(`Running real ${stratName.toUpperCase()} backtest over ${selectedSymbol} candles...`, 'info');

    const capital = parseFloat(document.getElementById('bt-capital').value) || 500000;
    const riskPct = parseFloat(document.getElementById('bt-risk').value) || 1.5;
    const maxRiskINR = (capital * riskPct) / 100;

    let equity = capital;
    let equityHistory = [capital];
    let wins = 0;
    let losses = 0;
    let grossProfit = 0;
    let grossLoss = 0;
    let peakEquity = capital;
    let maxDrawdownPct = 0;

    // Run simulation over actual loaded candles
    for (let i = 5; i < state.candles.length - 1; i++) {
        const c = state.candles[i];
        const prevC = state.candles[i - 1];
        const nextC = state.candles[i + 1];

        let isSignal = false;
        if (stratName === 'ema') {
            isSignal = c.ema9 > c.ema21 && prevC.ema9 <= prevC.ema21 && c.rsi > 48;
        } else if (stratName === 'supertrend') {
            isSignal = c.close > c.vwap && c.stDir === 'UP';
        } else if (stratName === 'bb') {
            isSignal = c.low <= c.bbLower && c.rsi < 38;
        }

        if (isSignal) {
            const entryPrice = c.close;
            const exitPrice = nextC.close;
            const pnlPerShare = exitPrice - entryPrice;
            const qty = Math.max(1, Math.floor(maxRiskINR / (entryPrice * 0.01)));
            const tradePnL = pnlPerShare * qty;

            equity += tradePnL;
            equityHistory.push(equity);

            if (tradePnL >= 0) {
                wins++;
                grossProfit += tradePnL;
            } else {
                losses++;
                grossLoss += Math.abs(tradePnL);
            }

            if (equity > peakEquity) peakEquity = equity;
            const dd = ((peakEquity - equity) / peakEquity) * 100;
            if (dd > maxDrawdownPct) maxDrawdownPct = dd;
        }
    }

    const netProfit = equity - capital;
    const totalTrades = wins + losses;
    const winRate = totalTrades > 0 ? ((wins / totalTrades) * 100).toFixed(1) : "0.0";
    const profitFactor = grossLoss > 0 ? (grossProfit / grossLoss).toFixed(2) : (grossProfit > 0 ? "9.99" : "1.00");

    const profitSign = netProfit >= 0 ? "+" : "";
    document.getElementById('bt-net-profit').innerText = `${profitSign}₹${Math.round(netProfit).toLocaleString('en-IN')}`;
    document.getElementById('bt-net-profit').className = netProfit >= 0 ? "success" : "danger";
    document.getElementById('bt-winrate').innerText = `${winRate}% (${wins} Wins / ${losses} Losses)`;
    document.getElementById('bt-pf').innerText = profitFactor;
    document.getElementById('bt-drawdown').innerText = `-${maxDrawdownPct.toFixed(1)}%`;

    renderRealEquityChart(equityHistory);
    showToast(`Backtest complete! Executed ${totalTrades} real trades. Win Rate: ${winRate}%`, 'success');
}

function initEquityChart() {
    renderRealEquityChart([500000, 502000, 501500, 504000, 508000]);
}

function renderRealEquityChart(equityHistory) {
    const canvas = document.getElementById('equityCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;
    ctx.scale(dpr, dpr);

    const w = rect.width;
    const h = rect.height;

    ctx.fillStyle = '#0b0f19';
    ctx.fillRect(0, 0, w, h);

    if (equityHistory.length < 2) return;

    const minEq = Math.min(...equityHistory) * 0.995;
    const maxEq = Math.max(...equityHistory) * 1.005;

    ctx.strokeStyle = equityHistory[equityHistory.length - 1] >= equityHistory[0] ? '#10b981' : '#ef4444';
    ctx.lineWidth = 2;
    ctx.beginPath();

    equityHistory.forEach((eq, i) => {
        const x = (i / (equityHistory.length - 1)) * w;
        const y = h - ((eq - minEq) / (maxEq - minEq)) * h;
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
    });
    ctx.stroke();
}

// ==================== LIVE MARKET TICK REFRESH ====================
function startLiveTickSimulation() {
    // Periodically refresh real market data every 15 seconds
    setInterval(() => {
        generateCandleData();
    }, 15000);
}

async function simulateOrder(type) {
    const broker = state.activeBroker;
    const symbol = state.symbol;
    if (!state.candles || state.candles.length === 0) {
        showToast("⚠️ No market price available to place order.", "danger");
        return;
    }
    const last = state.candles[state.candles.length - 1];

    try {
        // Attempt to post to Flask backend API gateway
        const res = await fetch(`${getApiBaseUrl()}/api/execute_order`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                symbol: symbol,
                action: type,
                quantity: 150,
                price: last.close,
                broker: broker
            })
        });

        const data = await res.json();

        if (res.ok && data.status === 'success') {
            showToast(`🚀 ${data.message}`, 'success');
        } else {
            showToast(`❌ Order Rejected: ${data.message || 'Execution Failed'}`, 'danger');
        }
    } catch (e) {
        showToast(`⚠️ Connection Failed: Backend API server is offline! Start server.py.`, 'danger');
    }
}

async function testBrokerAuth(brokerName) {
    const isUpstox = brokerName.includes('Upstox');
    
    const payload = isUpstox ? {
        broker: 'Upstox',
        access_token: document.getElementById('upstox-api-secret').value // Using secret field as token input
    } : {
        broker: 'ICICI Direct Breeze',
        app_key: document.getElementById('icici-app-key').value,
        secret_key: document.getElementById('icici-secret-key').value,
        session_token: document.getElementById('icici-session').value
    };

    try {
        const res = await fetch(`${getApiBaseUrl()}/api/connect_broker`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const data = await res.json();
        
        if (res.ok) {
            state.activeBroker = brokerName;
            document.getElementById('active-broker-text').innerText = `${brokerName} Connected`;
            showToast(`✅ ${data.message}`, 'success');
        } else {
            showToast(`❌ Connection Failed: ${data.message}`, 'danger');
        }
    } catch (e) {
        showToast(`❌ Backend API is offline!`, 'danger');
    }
}

function showBrokerTab(brokerKey) {
    document.querySelectorAll('.b-tab').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.broker-panel').forEach(p => p.classList.remove('active'));

    event.target.classList.add('active');
    document.getElementById(`broker-${brokerKey}`).classList.add('active');
}

// Toast System
function showToast(msg, type = 'info') {
    const container = document.getElementById('toast-container');
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.innerHTML = `<i class="fa-solid fa-circle-check"></i> <span>${msg}</span>`;
    container.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, 4000);
}

function copyCode(elementId) {
    const codeText = document.getElementById(elementId).innerText;
    navigator.clipboard.writeText(codeText);
    showToast('Python Code Copied to Clipboard!', 'success');
}

// ==================== MOBILE NAVIGATION DRAWER & RESIZE HELPERS ====================
function initMobileDrawer() {
    const toggleBtn = document.getElementById('mobile-menu-toggle');
    const backdrop = document.getElementById('sidebar-backdrop');
    const sidebar = document.querySelector('.sidebar');

    if (toggleBtn && sidebar && backdrop) {
        toggleBtn.addEventListener('click', () => {
            sidebar.classList.toggle('mobile-open');
            backdrop.classList.toggle('active');
        });

        backdrop.addEventListener('click', () => {
            closeMobileSidebar();
        });
    }
}

function closeMobileSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const backdrop = document.getElementById('sidebar-backdrop');
    if (sidebar) sidebar.classList.remove('mobile-open');
    if (backdrop) backdrop.classList.remove('active');
}

// Debounced Window Resize Handler for Canvas Re-rendering
let resizeTimeout;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
        const activeTab = document.querySelector('.tab-content.active');
        if (activeTab && activeTab.id === 'chart-studio') {
            renderMainChart();
            renderRsiChart();
        }
    }, 150);
});
