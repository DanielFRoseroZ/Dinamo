import React from 'react'



export const Singup = () => {
  return (
   <>
    
    <div class="row m-0 p-0 bg-landing justify-content-center"> 

      <div class="estilo-title">
            <p>
              <strong> Registrarse </strong>
            </p>
      </div>

      <div class="estilo-label">
        <label htmlFor="doc">Documento*</label>  
      </div>

      <div class="estilo-input">
        <input type="text" id="doc" name="doc" required
              minLength={6} maxLength={10} size={20}
        ></input>  
      </div>

      <div class="estilo-label">
        <label htmlFor="name">Nombre(s)*</label>  
      </div>

      <div class="estilo-input">
        <input type="name" id="name" name="name" required
              minLength={3} maxLength={20} size={20}
        ></input>  

      </div>

      <div class="estilo-label">
        <label htmlFor="lastName">Apellido(s)*</label>  
      </div>

      <div class="estilo-input">
        <input type="lastName" id="lastName" name="lastName" required
              minLength={4} maxLength={20} size={20}
        ></input>

      </div>

      <div class="estilo-label">
        <label htmlFor="tel">Celular*</label>  
      </div>

      <div class="estilo-input">
        <input type="tel" id="tel" name="tel" required
              minLength={1} maxLength={10} size={5}
        ></input>

      </div>

            <div class="estilo-label">
        <label htmlFor="email">Correo electronico*</label>  
      </div>

      <div class="estilo-input">
        <input type="email" id="email" name="email" required
              maxLength={50} size={30}
        ></input>

      </div>

      <div class="estilo-label">
        <label htmlFor="password">Contraseña*</label>  
      </div>

      <div class="estilo-input">
        <input type="password" id="pwd" name="pwd" required
              minLength={4} maxLength={10} size={4}
        ></input>  

      </div>

      <div class="estilo-label">
        <label htmlFor="password">Confirmar contraseña*</label>  
      </div>

      <div class="estilo-input">
        <input type="password" id="pwd" name="pwd" required
              minLength={4} maxLength={10} size={4}
        ></input>  

      </div>


      <div >
        <div class="estilo-button">
        <input class="color-button" type='submit' name='cancelar' id='cancelar' value='Cancelar'/> &nbsp;&nbsp;&nbsp;&nbsp; <input class="color-button" type='submit' name='registrar' id='registrar' value='Registrar'/>
        </div>
      </div>


    </div> 
          
   </>
  )
}
