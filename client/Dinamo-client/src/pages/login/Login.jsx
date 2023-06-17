import React from 'react'



export const Login = () => {
  return (
   <>
    
    <div class="row m-0 p-0 bg-landing justify-content-center"> 

      <div class="estilo-title">
            <p>
              <strong> Inicio de sesión </strong>
            </p>
      </div>

      <div class="estilo-label">
        <label htmlFor="user">Usuario*</label>  
      </div>

      <div class="estilo-input">
        <input type="text" id="user" name="user" required
              minLength={4} maxLength={10} size={4}
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

      <div >
        <div class="estilo-button">
        <button type="submit" value="button" class="color-button">Validar</button>
        </div>
      </div>


    </div> 
          
   </>
  )
}
