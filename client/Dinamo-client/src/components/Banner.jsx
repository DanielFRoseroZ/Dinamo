import {Logo} from '../assets/images'

export const Banner = () =>{
    return(
        <div class="row text-center m-0 p-0 estilo-titulo">
        <div class="col-12 m-0 p-0">
          <div class="row m-0 p-0 align-items-center justify-content-center">
            <div class="col-2 m-0 p-0">
              <img src={Logo} title="" alt="" class="img-fluid w-100" />
            </div>
            <div class="col-2 m-0 p-0">
              <button type="button" class="btn btn-style-1">Busqueda de Vehículos</button>
            </div>
            <div class="col-2 m-0 p-0">
              <button type="button" class="btn btn-style-1">Revisión y Reparación</button>
            </div>
            <div class="col-2 m-0 p-0">
              <button type="button" class="btn btn-style-1">Quejas y Reclamos</button>
            </div>
            <div class="col-2 m-0 p-0">
              <button type="button" class="btn btn-style-1">Ingresar</button>
            </div>
            <div class="col-2 m-0 p-0">
              <button type="button" class="btn btn-style-1">Registrarse</button>
            </div>
          </div>
        </div>


      </div>
    )
}