document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('aiForm');
  const resultEl = document.getElementById('result');
  if (!form) return;

  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    const data = {
      company: form.company.value,
      industry: form.industry.value,
      tone: form.tone.value
    };

    resultEl.textContent = "⏳ AI skriver...";

    try {
      const response = await fetch('https://crew-v9ht.onrender.com/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });

      if (!response.ok) throw new Error("Fejl i API");
      const result = await response.json();
      resultEl.textContent = result.result;
    } catch (err) {
      resultEl.textContent = "⚠️ Der opstod en fejl. Prøv igen.";
    }
  });
});
