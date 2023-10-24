import { useEffect, useState } from "react";

const Card = ({id, title, description, state, onDeleted, details}) => {
    
    const handleDelete = async () => {
        try {
            const response = await fetch(`https://oati-back.redflox.com/api/tutorial/${id}`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const responseData = await response.json();

            if (onDeleted) {
                onDeleted(id);
            }
        } catch (error) {
            console.error('Error al eliminar el tutorial:', error);
        }
    };


    return (
        <>
        { state ? 
        <div className="max-w-2xl p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 mb-2">
            <a href="#">
                <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{title}</h5>
            </a>
            <p className="mb-3 font-normal text-gray-700 dark:text-gray-400">{description}</p>
            
            <button 
                type="button" 
                className="focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-900"
                onClick={handleDelete}
            >
                Eliminar tutorial 
            </button>
            {
                details ? 
                <div className="text-sm font-medium text-gray-500 dark:text-gray-300">
                    {details.creator_user} <p className="text-blue-700 hover:underline dark:text-blue-500">{details.creation_date}</p>
                </div>
                :
                <></>
            }
            
        </div>
        : <></> }
        </>
    )
}

export default Card;
