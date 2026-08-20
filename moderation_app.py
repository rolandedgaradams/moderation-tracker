<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Question Paper Moderation Tracker</title>
<style>
  :root{
    --maroon:#6b1f2b;
    --dark:#222;
    --grey:#f2f2f2;
    --border:#b9b9b9;
  }
  *{box-sizing:border-box}
  body{
    margin:0;
    font-family:Arial,Helvetica,sans-serif;
    color:var(--dark);
    background:#e9e9e9;
  }
  .page{
    max-width:1500px;
    margin:20px auto;
    background:white;
    padding:24px;
    box-shadow:0 2px 10px #999;
  }
  h1{margin:0;color:var(--maroon);font-size:28px}
  .subtitle{margin:5px 0 18px;color:#555}
  .toolbar{
    display:flex;flex-wrap:wrap;gap:8px;margin-bottom:18px;
  }
  button{
    border:1px solid #777;
    background:#fff;
    padding:9px 13px;
    border-radius:4px;
    cursor:pointer;
    font-weight:bold;
  }
  button.primary{background:var(--maroon);color:white;border-color:var(--maroon)}
  button:hover{filter:brightness(.95)}
  .dashboard{
    display:grid;
    grid-template-columns:repeat(9,minmax(100px,1fr));
    gap:8px;
    margin-bottom:20px;
  }
  .card{
    border:1px solid var(--border);
    padding:10px;
    text-align:center;
    background:#fafafa;
  }
  .card .num{font-size:24px;font-weight:bold;color:var(--maroon)}
  .card .label{font-size:11px;text-transform:uppercase;margin-top:4px}
  .section-title{
    background:var(--maroon);
    color:#fff;
    padding:9px 12px;
    font-weight:bold;
    margin-top:18px;
  }
  table{
    width:100%;
    border-collapse:collapse;
    table-layout:fixed;
  }
  th,td{
    border:1px solid var(--border);
    padding:6px;
    font-size:12px;
    vertical-align:middle;
  }
  th{
    background:#ddd;
    text-align:center;
    font-weight:bold;
  }
  td[contenteditable="true"]{
    background:#fffef4;
    min-height:28px;
  }
  select{
    width:100%;
    border:0;
    background:transparent;
    font-size:12px;
    min-height:25px;
  }
  input[type="date"]{
    width:100%;
    border:0;
    background:transparent;
    font-size:11px;
  }
  .status{
    font-weight:bold;
    text-align:center;
  }
  .status-not{background:#f3f3f3}
  .status-progress{background:#fff2cc}
  .status-ready{background:#d9ead3}
  .status-submitted{background:#cfe2f3}
  .status-with{background:#c9daf8}
  .status-corrections{background:#f4cccc}
  .status-done{background:#d9ead3}
  .status-resubmitted{background:#eadcf8}
  .status-approved{background:#b6d7a8}
  .status-filed{background:#93c47d}
  .small{font-size:10px;color:#555}
  .footer{
    margin-top:18px;
    display:flex;
    justify-content:space-between;
    font-size:11px;
    color:#555;
  }
  .legend{
    display:flex;flex-wrap:wrap;gap:7px;margin:10px 0;
  }
  .legend span{
    border:1px solid #bbb;padding:4px 7px;font-size:10px;
  }
  .actions-table th,.actions-table td{font-size:11px}
  @media(max-width:1100px){
    .page{margin:0;padding:12px}
    .dashboard{grid-template-columns:repeat(3,1fr)}
    table{min-width:1200px}
    .table-wrap{overflow-x:auto}
  }
  @media print{
    body{background:white}
    .page{margin:0;max-width:none;box-shadow:none;padding:10px}
    .toolbar{display:none}
    .dashboard{grid-template-columns:repeat(9,1fr)}
    .section-title{break-after:avoid}
    table{font-size:9px}
    th,td{font-size:9px;padding:4px}
    .no-print{display:none}
    @page{size:A4 landscape;margin:8mm}
  }
</style>
</head>
<body>
<div class="page">
  <h1>Question Paper Moderation Tracker</h1>
  <div class="subtitle">Year 2 and Year 3 • Question Papers for Moderation</div>

  <div class="toolbar">
    <button class="primary" onclick="window.print()">Print / Save as PDF</button>
    <button onclick="addRow()">Add Paper</button>
    <button onclick="saveData()">Save</button>
    <button onclick="loadData()">Load Saved Data</button>
    <button onclick="clearSaved()">Clear Saved Data</button>
  </div>

  <div class="dashboard" id="dashboard"></div>

  <div class="section-title">Moderation Tracker</div>
  <div class="legend">
    <span>NOT STARTED</span><span>IN PROGRESS</span><span>READY FOR MODERATION</span>
    <span>SUBMITTED</span><span>WITH MODERATOR</span><span>CORRECTIONS REQUIRED</span>
    <span>CORRECTIONS DONE</span><span>RESUBMITTED</span><span>APPROVED</span><span>FILED</span>
  </div>

  <div class="table-wrap">
  <table id="tracker">
    <thead>
      <tr>
        <th style="width:4%">Year</th>
        <th style="width:13%">Subject</th>
        <th style="width:8%">Task</th>
        <th style="width:8%">Assessment</th>
        <th style="width:10%">Moderator</th>
        <th style="width:13%">Status</th>
        <th style="width:8%">Date Submitted</th>
        <th style="width:8%">Date Returned</th>
        <th style="width:13%">Moderator Feedback</th>
        <th style="width:13%">Outstanding Action</th>
        <th style="width:2%">✓</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>
  </div>

  <div class="section-title">Moderator Details</div>
  <div class="table-wrap">
  <table id="moderators">
    <thead>
      <tr>
        <th style="width:15%">Moderator</th>
        <th style="width:20%">Subject</th>
        <th style="width:10%">Year</th>
        <th style="width:20%">Contact / Email</th>
        <th style="width:35%">Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr><td contenteditable="true">B. KOENZE</td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td></tr>
      <tr><td contenteditable="true">D. DAVIDS</td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td></tr>
      <tr><td contenteditable="true">K. ABRAHAMS</td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td></tr>
      <tr><td contenteditable="true">S. ST JERRY</td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td></tr>
      <tr><td contenteditable="true">U. DE VILLIERS</td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td></tr>
      <tr><td contenteditable="true">A. PRESSEND</td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td></tr>
      <tr><td contenteditable="true">M. MURRAY</td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td><td contenteditable="true"></td></tr>
    </tbody>
  </table>
  </div>

  <div class="section-title">Action Required</div>
  <div class="table-wrap">
  <table class="actions-table">
    <thead>
      <tr><th>Year</th><th>Subject</th><th>Task</th><th>Moderator</th><th>Status</th><th>Outstanding Action</th></tr>
    </thead>
    <tbody id="actions"></tbody>
  </table>
  </div>

  <div class="footer">
    <span>Tip: Yellow cells are editable. Use the Status dropdowns to track each paper.</span>
    <span>Last updated: <span id="updated"></span></span>
  </div>
</div>

<script>
const papers = [
["Y2","Afrikaans Huistaal","Taak 3","Eksamen"],
["Y2","English FAL","Task 3","Exam"],
["Y2","Wiskunde","Taak 7",""],
["Y2","Wiskunde","Taak 8",""],
["Y2","Wiskunde","Taak 9","Eksamen"],
["Y2","Natuurwetenskap","Taak 5","Prakties"],
["Y2","Natuurwetenskap","Taak 6","Eksamen"],
["Y2","Liggaamlike Opvoeding","Taak 2","Prakties"],
["Y3","Afrikaans Huistaal","Taak 3","Eksamen"],
["Y3","English FAL","Task 3","Exam"],
["Y3","Wiskunde","Taak 7",""],
["Y3","Wiskunde","Taak 8",""],
["Y3","Wiskunde","Taak 9","Eksamen"],
["Y3","Natuurwetenskap","Taak 5","Prakties"],
["Y3","Natuurwetenskap","Taak 6","Eksamen"],
["Y3","Liggaamlike Opvoeding","Taak 2","Prakties"]
];

const statuses = [
"NOT STARTED","IN PROGRESS","READY FOR MODERATION","SUBMITTED","WITH MODERATOR",
"CORRECTIONS REQUIRED","CORRECTIONS DONE","RESUBMITTED","APPROVED","FILED"
];

function statusClass(s){
  return {
    "NOT STARTED":"status-not","IN PROGRESS":"status-progress",
    "READY FOR MODERATION":"status-ready","SUBMITTED":"status-submitted",
    "WITH MODERATOR":"status-with","CORRECTIONS REQUIRED":"status-corrections",
    "CORRECTIONS DONE":"status-done","RESUBMITTED":"status-resubmitted",
    "APPROVED":"status-approved","FILED":"status-filed"
  }[s] || "";
}

function makeSelect(value="NOT STARTED"){
  const sel=document.createElement("select");
  statuses.forEach(s=>{
    const o=document.createElement("option");
    o.value=s;o.textContent=s;
    if(s===value)o.selected=true;
    sel.appendChild(o);
  });
  sel.addEventListener("change",()=>{
    sel.parentElement.className=statusClass(sel.value);
    update();
  });
  sel.parentElement && (sel.parentElement.className=statusClass(value));
  return sel;
}

function addPaperRow(data){
  const tr=document.createElement("tr");
  tr.innerHTML=`
    <td contenteditable="true">${data?.[0]||""}</td>
    <td contenteditable="true">${data?.[1]||""}</td>
    <td contenteditable="true">${data?.[2]||""}</td>
    <td contenteditable="true">${data?.[3]||""}</td>
    <td></td>
    <td></td>
    <td><input type="date" value="${data?.[6]||""}"></td>
    <td><input type="date" value="${data?.[7]||""}"></td>
    <td contenteditable="true">${data?.[8]||""}</td>
    <td contenteditable="true">${data?.[9]||""}</td>
    <td><input type="checkbox" ${data?.[10]?"checked":""}></td>`;
  const moderatorCell=tr.children[4];
  const moderatorSelect=document.createElement("select");
  moderatorSelect.innerHTML=`<option value="">Select moderator</option>
    <option>B. KOENZE</option>
    <option>D. DAVIDS</option>
    <option>K. ABRAHAMS</option>
    <option>S. ST JERRY</option>
    <option>U. DE VILLIERS</option>
    <option>A. PRESSEND</option>
    <option>M. MURRAY</option>`;
  moderatorSelect.value=data?.[4]||"";
  moderatorCell.appendChild(moderatorSelect);

  const statusCell=tr.children[5];
  const select=makeSelect(data?.[5]||"NOT STARTED");
  statusCell.appendChild(select);
  statusCell.className=statusClass(data?.[5]||"NOT STARTED");
  select.addEventListener("change",update);
  tr.querySelectorAll("td, input, select").forEach(el=>{
    el.addEventListener("input",update);
    el.addEventListener("change",update);
  });
  document.querySelector("#tracker tbody").appendChild(tr);
}

function render(){
  const tbody=document.querySelector("#tracker tbody");
  tbody.innerHTML="";
  papers.forEach(p=>addPaperRow(p));
  update();
}

function addRow(){
  addPaperRow(["Y","","","","","NOT STARTED","","","","",false]);
  update();
}

function getRows(){
  return [...document.querySelectorAll("#tracker tbody tr")].map(tr=>{
    const c=tr.children;
    return [
      c[0].innerText.trim(),c[1].innerText.trim(),c[2].innerText.trim(),c[3].innerText.trim(),
      c[4].querySelector("select").value,c[5].querySelector("select").value,c[6].querySelector("input").value,
      c[7].querySelector("input").value,c[8].innerText.trim(),c[9].innerText.trim(),
      c[10].querySelector("input").checked
    ];
  });
}

function update(){
  const rows=getRows();
  const counts={};
  statuses.forEach(s=>counts[s]=0);
  rows.forEach(r=>counts[r[5]]=(counts[r[5]]||0)+1);

  document.getElementById("dashboard").innerHTML=[
    ["TOTAL",rows.length],
    ...statuses.map(s=>[s,counts[s]||0])
  ].map(x=>`<div class="card"><div class="num">${x[1]}</div><div class="label">${x[0]}</div></div>`).join("");

  const actionRows=rows.filter(r=>r[5]!=="APPROVED" && r[5]!=="FILED");
  document.getElementById("actions").innerHTML=actionRows.length
    ? actionRows.map(r=>`<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td><td>${r[4]}</td><td class="${statusClass(r[5])}">${r[5]}</td><td>${r[9]||""}</td></tr>`).join("")
    : `<tr><td colspan="6" style="text-align:center">No outstanding action.</td></tr>`;

  document.getElementById("updated").textContent=new Date().toLocaleString();
}

function saveData(){
  const data={
    tracker:getRows(),
    moderators:[...document.querySelectorAll("#moderators tbody tr")].map(tr=>[...tr.children].map(td=>td.innerText))
  };
  localStorage.setItem("questionPaperModerationTracker",JSON.stringify(data));
  alert("Tracker saved on this device.");
}

function loadData(){
  const raw=localStorage.getItem("questionPaperModerationTracker");
  if(!raw){alert("No saved tracker found on this device.");return;}
  const data=JSON.parse(raw);
  document.querySelector("#tracker tbody").innerHTML="";
  (data.tracker||[]).forEach(p=>addPaperRow(p));
  const mt=document.querySelector("#moderators tbody");
  mt.innerHTML="";
  (data.moderators||[]).forEach(row=>{
    const tr=document.createElement("tr");
    row.forEach(v=>{const td=document.createElement("td");td.contentEditable="true";td.innerText=v;tr.appendChild(td)});
    mt.appendChild(tr);
  });
  update();
}

function clearSaved(){
  if(confirm("Delete the saved copy from this device?")){
    localStorage.removeItem("questionPaperModerationTracker");
    alert("Saved copy deleted.");
  }
}

document.querySelectorAll("#moderators td").forEach(td=>td.addEventListener("input",update));
render();
</script>
</body>
</html>
