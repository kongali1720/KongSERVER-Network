// server_status.js
// Monitoring dasar untuk KongSERVER

const os = require('os');

function bytesToMB(bytes) {
    return (bytes / 1024 / 1024).toFixed(2);
}

console.log("=== KongSERVER Status ===");
console.log("Hostname:", os.hostname());
console.log("Platform:", os.platform(), os.release());
console.log("Uptime:", (os.uptime() / 3600).toFixed(2), "hours");
console.log("CPU Cores:", os.cpus().length);
console.log("Load Average (1m, 5m, 15m):", os.loadavg().map(avg => avg.toFixed(2)).join(", "));
console.log("Total Memory:", bytesToMB(os.totalmem()), "MB");
console.log("Free Memory:", bytesToMB(os.freemem()), "MB");
console.log("Used Memory:", bytesToMB(os.totalmem() - os.freemem()), "MB");
