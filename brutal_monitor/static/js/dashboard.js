async function refreshDashboard() {
  if (!document.getElementById('total-count')) return;
  try {
    const summary = await fetch('/api/resumen/').then(r => r.json());
    document.getElementById('total-count').textContent = summary.total;
    document.getElementById('online-count').textContent = summary.online;
    document.getElementById('offline-count').textContent = summary.offline;
    const uptime = summary.total ? ((summary.online / summary.total) * 100).toFixed(2) : '100.00';
    document.getElementById('uptime-count').textContent = `${uptime}%`;

    const logData = await fetch('/api/logs/').then(r => r.json());
    const body = document.getElementById('logs-body');
    if (!body) return;
    body.innerHTML = logData.logs.map(l => `
      <tr>
        <td>${new Date(l.checked_at).toLocaleString()}</td>
        <td>${l.service}</td>
        <td><span class="badge ${l.is_up ? 'bg-success' : 'bg-danger'}">${l.is_up ? 'UP' : 'DOWN'}</span></td>
        <td>${l.status_code ?? '-'}</td>
        <td>${l.response_time_ms} ms</td>
        <td>${l.error_message || '-'}</td>
      </tr>
    `).join('');
  } catch (err) {
    console.error('Error actualizando dashboard', err);
  }
}

setInterval(refreshDashboard, 1000);
