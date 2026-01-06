import { useState, useEffect } from "react"

function App() {
    const[projects, setProjects] = useState([]);

    useEffect(() => {

        fetch("http://localhost:8000/api/projects")
            .then(response => response.json())
            .then(data => {
                setProjects(data)
            })
            .catch(err => console.error("Erro ao ligar ao server:", err));


    }, []);

return (
    <div style={{ padding: '20px', backgroundColor: '#000', color: '#fff' }}>
      <h1>Os Meus Projetos</h1>

      {/* Se a lista estiver vazia, mostra aviso. Se tiver dados, faz o loop */}
      {projects.length === 0 ? (
        <p>A carregar...</p>
      ) : (
        projects.map((p, index) => (
          <div key={index} style={{ border: '1px solid #333', margin: '10px 0', padding: '15px' }}>
            <h2>{p.title}</h2>
            <p>{p.desc}</p>
            <div>
              {p.tech.map(t => <span key={t} style={{ marginRight: '10px', color: '#00ff00' }}>{t}</span>)}
            </div>
          </div>
        ))
      )}
    </div>
  );
}

export default App;
