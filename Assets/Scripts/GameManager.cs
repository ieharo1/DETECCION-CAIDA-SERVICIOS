using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    public GameObject menuPrincipal;
    public GameObject menuGameOver;


    public float velocidad = 2;
    public GameObject col;
    public Renderer fondo;
    public GameObject piedra1;
    public GameObject piedra2;
    public GameObject flores1;
    public GameObject flores2;
    public GameObject flores3;
    public GameObject flores4;
    public GameObject carnivora;
    public GameObject koopa1;
    public GameObject koopa2;
    public GameObject dragon;


    /*GAME OVER*/
    public bool gameOver = false;
    public bool start = false;


    public List<GameObject> cols;
    public List<GameObject> obstaculos;
    public List<GameObject> adornos;
    public List<GameObject> plantacarnivora;
    public List<GameObject> koopa;
    public List<GameObject> dragones;
    // Start is called before the first frame update
    void Start()
    {
        //Crear Mapa
        for (int i=0; i<21;i++)
        {
            cols.Add(Instantiate(col, new Vector2(-10 + i, -3), Quaternion.identity));
        }
        //Crear Piedras
        obstaculos.Add(Instantiate(piedra1, new Vector2(9, -2), Quaternion.identity));
        
        //Crear Flores
        adornos.Add(Instantiate(flores1, new Vector2(7, -2), Quaternion.identity));
        adornos.Add(Instantiate(flores2, new Vector2(2, -2), Quaternion.identity));
        adornos.Add(Instantiate(flores3, new Vector2(1, -2), Quaternion.identity));
        adornos.Add(Instantiate(flores4, new Vector2(14, -2), Quaternion.identity));

        //PLANTA CARNIVORA
        plantacarnivora.Add(Instantiate(carnivora, new Vector2(9, -2.092f), Quaternion.identity));

        //Koopa
        koopa.Add(Instantiate(koopa1, new Vector2(12, -2), Quaternion.identity));
        koopa.Add(Instantiate(koopa2, new Vector2(6, -2), Quaternion.identity));

        //Dragones
        dragones.Add(Instantiate(dragon, new Vector2(13, 3), Quaternion.identity));


    }
    // Update is called once per frame
    void Update()
    {
        if (start == false)
        {
            if (Input.GetKeyDown(KeyCode.X))
            {
                start = true;
            }
        }
        if (start==true && gameOver == true)
        {
            menuGameOver.SetActive(true);//activa el menu
            if (Input.GetKeyDown(KeyCode.X))
            {
                SceneManager.LoadScene(SceneManager.GetActiveScene().name);
            }
        }
        if (start == true && gameOver == false)
        {
            menuPrincipal.SetActive(false);//desactiva el menu al comenzar el juego
            fondo.material.mainTextureOffset = fondo.material.mainTextureOffset + new Vector2(0.02f, 0) * Time.deltaTime;
            //Time.deltaTime= que se mueva siempre a la misma velocidad no importa el rendimiento de la computadora
            //Vector2 es para dar dos posiciones en una dimension 2d (x y)
            //MOVER MAPA
            for (int i = 0; i < cols.Count; i++)
            {
                if (cols[i].transform.position.x <= -10)
                {
                    cols[i].transform.position = new Vector3(10, -3, 0);
                }
                cols[i].transform.position = cols[i].transform.position + new Vector3(-1, 0, 0) * Time.deltaTime * velocidad;
            }
            //MOVER OBSTACULOS
            for (int i = 0; i < obstaculos.Count; i++)
            {
                if (obstaculos[i].transform.position.x <= -10)
                {
                    float randomObs = Random.Range(11, 18);
                    obstaculos[i].transform.position = new Vector3(randomObs, -2, 0);
                }
                obstaculos[i].transform.position = obstaculos[i].transform.position + new Vector3(-1, 0, 0) * Time.deltaTime * velocidad;
            }
            //MOVER ADORNOS
            for (int i = 0; i < adornos.Count; i++)
            {
                if (adornos[i].transform.position.x <= -10)
                {
                    float randonmAdor = Random.Range(11, 18);
                    adornos[i].transform.position = new Vector3(randonmAdor, -2, 0);
                }
                adornos[i].transform.position = adornos[i].transform.position + new Vector3(-1, 0, 0) * Time.deltaTime * velocidad;
            }
            //MOVER PLANTA CARNIVORA
            for (int i = 0; i < plantacarnivora.Count; i++)
            {
                if (plantacarnivora[i].transform.position.x <= -10)
                {
                    float randomCarn = Random.Range(11, 18);
                    plantacarnivora[i].transform.position = new Vector3(randomCarn, -2.092f, 0);
                }
                plantacarnivora[i].transform.position = plantacarnivora[i].transform.position + new Vector3(-1, 0, 0) * Time.deltaTime * velocidad;
            }
            //MOVER KOOPA
            for (int i = 0; i < koopa.Count; i++)
            {
                if (koopa[i].transform.position.x <= -10)
                {
                    float randomKop = Random.Range(11, 18);
                    koopa[i].transform.position = new Vector3(randomKop, -2, 0);
                }
                koopa[i].transform.position = koopa[i].transform.position + new Vector3(-1, 0, 0) * Time.deltaTime * velocidad * 2;
            }
            //MOVER DRAGON

            for (int i = 0; i < dragones.Count; i++)
            {
                if (dragones[i].transform.position.x <= -10)
                {
                    float randomDrag = Random.Range(11, 19);
                    float updown = Random.Range(0, 2);
                    dragones[i].transform.position = new Vector3(randomDrag, updown, 0);
                }
                dragones[i].transform.position = dragones[i].transform.position + new Vector3(-1, 0, 0) * Time.deltaTime * velocidad * 3;
            }
        }

    }
}
