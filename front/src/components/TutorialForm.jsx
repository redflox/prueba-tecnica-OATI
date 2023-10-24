import React, { useState } from 'react';

function TutorialForm({ onNewTutorial }) {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [creatorUser, setCreatorUser] = useState('');
    const [state, setState] = useState(true); // Por defecto será true

    const getCurrentDate = () => {
        const today = new Date();
        return `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`;
    };

    const submitData = async () => {
        const currentDate = getCurrentDate();

        const data = {
            tutorial: {
                title,
                description,
                state
            },
            details: {
                creation_date: currentDate,
                creator_user: creatorUser
            }
        };

        const resetForm = () => {
            setTitle('');
            setDescription('');
            setCreatorUser('');
            setState(true);
        };

        try {
            const response = await fetch('https://oati-back.redflox.com/api/tutorial/detail', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const responseData = await response.json();


            if (onNewTutorial) {
                onNewTutorial(responseData);
            }

            resetForm();
        } catch (error) {
            console.error('Error al hacer la petición:', error);
        }
    };

    return (
        <div className="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl m-5 p-6">
            <div>
                <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Título:</label>
                    <input className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" type="text" value={title} onChange={e => setTitle(e.target.value)} />
                </div>
                <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Descripción:</label>
                    <input className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" type="text" value={description} onChange={e => setDescription(e.target.value)} />
                </div>
                <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Creador:</label>
                    <input className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" type="text" value={creatorUser} onChange={e => setCreatorUser(e.target.value)} />
                </div>
                <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Estado:</label>
                    <label>
                        <input className="w-4 h-4 border-gray-300 focus:ring-2 focus:ring-blue-300 dark:focus:ring-blue-600 dark:focus:bg-blue-600 dark:bg-gray-700 dark:border-gray-600" type="radio" value="true" checked={state === true} onChange={() => setState(true)} />
                        Activo
                    </label>
                    <label>
                        <input className="w-4 h-4 border-gray-300 focus:ring-2 focus:ring-blue-300 dark:focus:ring-blue-600 dark:focus:bg-blue-600 dark:bg-gray-700 dark:border-gray-600" type="radio" value="false" checked={state === false} onChange={() => setState(false)} />
                        Inactivo
                    </label>
                </div>
                <button className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800" onClick={submitData}>Enviar</button>
            </div>
        </div>
    );
}

export default TutorialForm;
