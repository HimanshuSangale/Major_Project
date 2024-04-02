// eslint-disable-next-line no-unused-vars
import React from 'react'

import "./SearchResultsList.css";
import { SearchResult } from './SearchResult';

// eslint-disable-next-line react/prop-types
export const SearchResultsList = ({ results }) => {
    return (
        <div className='results-list'>
            {
                // eslint-disable-next-line react/prop-types
                results.map((result, id) => {
                    return <SearchResult result = {result} key = {id}/>
                })
            }
        </div>
    )
}
