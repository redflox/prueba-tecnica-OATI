import React, { useState, useEffect } from 'react';
import TutorialForm from './components/TutorialForm'
import Tutorials from './components/Tutorials'

function App() {
    const [tutorials, setTutorials] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch('https://oati-back.redflox.com/api/tutorial/detail')
        .then(response => {
            if (!response.ok){
                throw new Error('Network error');
            }
            return response.json();
        })
        .then(data => {
            setTutorials(data);
            setLoading(false);
        })
        .catch(error => {
            console.error("Error fetching tutorials:", error);
            setLoading(false);
        });
    }, []);

    const addTutorialToList = (tutorial) => {
        setTutorials(prevTutorials => [...prevTutorials, {
          title: tutorial.tutorial.title,
          description: tutorial.tutorial.description,
          state: tutorial.tutorial.state,
          id: tutorial.tutorial.id,
          detail: {
            creation_date: tutorial.details.creation_date,
            creator_user: tutorial.details.creator_user
          }
        }]);
    };

    const handleTutorialDeleted = (id) => {
      setTutorials(prevData => prevData.filter(tutorial => tutorial.id !== id));
    };

    return (
        <>
            <TutorialForm onNewTutorial={addTutorialToList} />
            {loading ? 'Cargando...' : <Tutorials tutorials={tutorials} onDeleteTutorial={handleTutorialDeleted} />}
        </>
    );
}

export default App;
