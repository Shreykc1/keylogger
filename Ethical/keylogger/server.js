const express = require('express');
const app = express();
app.use(express.json());


app.post('/', (req, res) => {
    const { loggedTexts } = req.body;
    console.log(loggedTexts);
    res.status(200).send('Data received'); // Send a response back
});


app.listen(8000, () => {
    console.log('Server is running at port: 8000');
});
