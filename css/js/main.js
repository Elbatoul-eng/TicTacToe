const projects = [
  {title:'Tic-Tac-Toe IA',desc:'Jeu Tic-Tac-Toe avec IA basique',link:'#'},
  {title:'To-Do List',desc:'Gestion de tâches locale',link:'#'},
  {title:'Landing Marketing',desc:'Landing page responsive',link:'#'},
];

const container = document.getElementById('projects-list');
projects.forEach(p=>{
  const div = document.createElement('div');
  div.className = 'project-card';
  div.innerHTML = `<h3>${p.title}</h3><p>${p.desc}</p><a href="${p.link}" target="_blank">Voir</a>`;
  container.appendChild(div);
});

// Dark Mode toggle
const toggleBtn = document.getElementById('darkModeToggle');
toggleBtn.addEventListener('click', ()=>{
  document.body.classList.toggle('dark');
  localStorage.setItem('darkMode', document.body.classList.contains('dark') ? '1':'0');
});

// Load saved preference
if(localStorage.getItem('darkMode')==='1'){
  document.body.classList.add('dark');
}
