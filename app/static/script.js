```javascript
const tabs = document.querySelectorAll(".tab");
const panels = document.querySelectorAll(".panel");

tabs.forEach(tab => {
  tab.addEventListener("click", () => {
    tabs.forEach(t => t.classList.remove("active"));
    panels.forEach(p => p.classList.remove("active"));
    tab.classList.add("active");
    document.getElementById(tab.dataset.target).classList.add("active");
  });
});

async function sendQuery(agent) {
  const input = document.getElementById(`input-${agent}`);
  const output = document.getElementById(`output-${agent}`);
  const query = input.value.trim();
  output.textContent = "Loading...";
  try {
    const res = await fetch(`/api/chat/${agent}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });
    const data = await res.json();
    output.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    output.textContent = `Error: ${err}`;
  }
}
```
