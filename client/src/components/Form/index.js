import React, {useState} from 'react'

function Form() {
    const [url, setUrl] = useState('')
    const[shorturl, setShortUrl] = useState('')
    const[longurl, setLongUrl] = useState('')

    const handleInput = (e) => {
        setUrl(e.target.value)

    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        const options = {
            method: 'POST',
            body: JSON.stringify({url_original: url}),
            headers: {'Content-Type': 'application/json'}

        }
        const response = await fetch('http://127.0.0.1:8000/url/',options)
        const response_obj = await response.json()
        setShortUrl(response_obj.url_short)
        setLongUrl(response_obj.original_url)
    }
  return (
    <>
    <form onSubmit={handleSubmit}>
        <label htmlFor='URL'>Enter URL:</label>
        <input type='url' id='url' name='url' onChange={handleInput}></input>
        <button type='Submit'>Submit</button>
    </form>
    {shorturl && (
        <>
          <p>Your short link is:</p>
          <a href={shorturl}>{shorturl}</a>
        </>
      )}
    </>
  )
}

export default Form
