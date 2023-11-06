const express = require('express');
const app = express();
const {spawn} = require('child_process');

const {textos} = require('./textos')

//Router
const routerMexico = express.Router();
app.use('/api/textos/mexico', routerMexico);

routerMexico.use(express.json());


app.get('/' ,(req, res) => {

    // Cambiar estos textos por los recogidos de la API 
    let texto1 = "No te sientas obligado a realizarme una donación, pero cada aportación me ayuda a mantener el sitio en activo para que continúe existiendo y me motiva a continuar creando nuevo contenido."
    let texto2 = "No te sientas obligado a realizarme una aportación, pero cada donación me ayuda a mantener el sitio online para que continúe existiendo y me motiva a seguir haciendo nuevo contenido."

    const python = spawn('python3', ['textComp.py', texto1, texto2]);

    //python.stdin.write("Ale");
    //python.stdin.end();

    let dataToSend = '';
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
    });

    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // send data to browser
        res.send(dataToSend)
    });

    //res.send('Mi primer server con express');
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