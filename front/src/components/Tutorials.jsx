import Card from './Card'
import { useEffect, useState } from 'react'

const Tutorials = ({tutorials, onDeleteTutorial}) => {

    const [data, setData] = useState(tutorials)

    useEffect( () => {
        setData(tutorials.slice().reverse())
    }, [tutorials])

    if (!data) return null

    return (
        <div className="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl m-5 p-6">
            {data.map( tutorial => {
                return (
                    <Card 
                        key={tutorial.id} 
                        id={tutorial.id} 
                        title={tutorial.title} 
                        description={tutorial.description} 
                        state={tutorial.state}
                        onDeleted={onDeleteTutorial}
                        details={tutorial.detail}
                    />
                )
            })}
        </div>
    )
}

export default Tutorials;
