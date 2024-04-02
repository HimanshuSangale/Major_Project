/* eslint-disable no-unused-vars */
import React, { useState } from 'react'

import { FaSearch } from "react-icons/fa"

import "./SearchBar.css"

// eslint-disable-next-line react/prop-types
export const SearchBar = ({ setResults }) => {
    const [input, setInput] = useState("")

    const fetchData = (value) => {
        fetch("http://127.0.0.1:5000/process_query", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(value),
        })
            .then((response) => response.json())
            // writing {response.json()} in curly braces need a 
            // explicit return statement to pass values to next then
            // .then((json) => {
            //     const results = json.filter((keywords) => {
            //         return value && user && user.name && user.name.toLowerCase().includes(value)
            //     })/process_query?query=${enc
            //     setResults(results);
            // });
            .then((json) => {
                // Access the array elements
                // console.log(json[0])
                const results = [];
                for (let key in json) {
                    results.push(json[key]);
                }
                console.log(results);
                // const results = json.map(element => element);
                setResults(results);
            })
    };

    // const handleChange = (value) => {
    //     setInput(value);
    //     const input = { query: value }
    //     fetchData(input);
    // };
    const handleChange = (value) => {
        setInput(value);

        // Split the input value into words
        // const words = value.trim().split(" ");

        // Send fetch request only if there are two or more words
        if (value.length >= 6) {
            const input = { query: value };
            console.log("Request sent")
            fetchData(input);
        } else {
            // Clear the results if there are less than two words
            console.log("Request not sent")
            setResults([]);
        }
    };


    return (
        <div className='input-wrapper'>
            <FaSearch id='search-icon' />
            <input placeholder='Type to search..'
                value={input}
                onChange={(e) => handleChange(e.target.value)} />
        </div>
    )
}
