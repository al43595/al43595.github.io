import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          You are the main character to your own story
        </p>
        <a
          className="App-link"
          href="albertlu.studio"
          target="_blank"
          rel="noopener noreferrer"
        >
          View Portfolio
        </a>
        <button onClick={() => joinProject('some_project_id')} style={{ marginTop: '20px' }}>
          Join Project
        </button>
      </header>
      
    </div>
  );
}

function joinProject(projectId) {
  fetch(`http://127.0.0.1:5000/join/${projectId}`)
    .then(response => response.json())
    .then(data => {
      console.log(data);
      alert(data.message);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}


export default App;
