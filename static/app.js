document.getElementById('send').addEventListener('click', sendPrompt);

async function sendPrompt(){
  const promptEl = document.getElementById('prompt');
  const responseEl = document.getElementById('response');
  const base = document.getElementById('baseUrl').value || '';
  const prompt = promptEl.value.trim();
  if(!prompt){ responseEl.textContent = 'Escribe un prompt.'; return; }

  const url = `${base}/llm/${encodeURIComponent(prompt)}`;
  responseEl.textContent = 'Cargando...';
  try{
    const res = await fetch(url);
    if(!res.ok) throw new Error('HTTP ' + res.status);
    const data = await res.json();
    responseEl.textContent = data.respuesta ?? JSON.stringify(data, null, 2);
  }catch(err){
    responseEl.textContent = 'Error: ' + err.message + '\n\nComprueba que el backend está en ejecución y que CORS está habilitado.';
  }
}
