const express = require('express');
const app = express();

const {textos} = require('./textos')

//Router
const routerMexico = express.Router();
app.use('/api/textos/mexico', routerMexico);

routerMexico.use(express.json());


app.get('/' ,(req, res) => {
    res.send('Mi primer server con express');
});

routerMexico.get('/:estilo', (req, res) =>{
    const estilo = req.params.estilo;

    console.log (textos.mexico);
    const resultado = textos.mexico.filter(texto => texto.estilo === estilo);

    if(resultado.length === 0)
        return res.status(404).send(`No se encuentran textos de ${estilo} en mexico`);

        res.send(JSON.stringify(resultado));
    //res.send(textos.)
});

routerMexico.post('/', (req, res)=> {
    const nuevoTexto = req.body;
    textos.mexico.push(nuevoTexto);
    res.send(JSON.stringify(textos.mexico));
});

const PUERTO = process.env.PORT || 3000;

app.listen(PUERTO, ()=>{
    console.log(`El servidor está escuchando en el puperto ${PUERTO}...`);
});