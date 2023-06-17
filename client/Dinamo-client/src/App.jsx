import { useState } from 'react'
import './css/style.css'

import {BYDDolphin,
  BYDYuanPlus,
  CheryeQ1,
  Logo,
  RenaultZOE,
  TeslaModel3,
  TeslaModelY,
  VolkswagenID4,
  WullingHongGuangMiniEV} from "./assets/images/index.js"
import { Banner } from './components/Banner'
import { Pqrs } from './pages/pqrs/Pqrs'
import { Login } from './pages/login/Login'
import { Singup } from './pages/singup/Singup'


function App() {

  return (
    <>
      <Singup />
    
      {/* <Banner />

      <div class="row m-0 p-0 bg-landing justify-content-center">
        <div class="col-12 m-0 p-0 estilo-1">
          <div class="row m-0 p-0">
            <p class="text-center estilo-dinamo-2 text-center my-5">
              <strong> Bienvenido al mundo de los carros eléctricos</strong>
            </p>
          </div>
        </div>
        <div class="col-12 m-0 p-0">
          <div class="swiper swiper-container sw-products ">
            <div class="swiper-wrapper">
              <div class="swiper-slide">
                <div class="row mx-0">
                  <div class="col-12 px-0">
                    <img src={BYDDolphin} title="" alt="" class="img-fluid w-100" />
                    <button type="button" class="btn">VER COLECCIÓN</button>
                  </div>
                </div>
              </div>
              <div class="swiper-slide">
                <div class="row mx-0">
                  <div class="col-12 px-0">
                    <img src={RenaultZOE} title="" alt="" class="img-fluid w-100" />
                    <button type="button" class="btn">VER COLECCIÓN</button>
                  </div>
                </div>
              </div>
              <div class="swiper-slide">
                <div class="row mx-0">
                  <div class="col-12 px-0">
                    <img src={TeslaModel3} title="" alt="" class="img-fluid w-100" />
                    <button type="button" class="btn">VER COLECCIÓN</button>
                  </div>
                </div>
              </div> 
              <div class="swiper-slide">
                <div class="row mx-0">
                  <div class="col-12 px-0">
                    <img src={TeslaModelY} title="" alt="" class="img-fluid w-100" />
                    <button type="button" class="btn">VER COLECCIÓN</button>
                  </div>
                </div>
              </div>
              <div class="swiper-slide">
                <div class="row mx-0">
                  <div class="col-12 px-0">
                    <img src={VolkswagenID4} title="" alt="" class="img-fluid w-100" />
                    <button type="button" class="btn">VER COLECCIÓN</button>
                  </div>
                </div>
              </div>
              <div class="swiper-slide">
                <div class="row mx-0">
                  <div class="col-12 px-0">
                    <img src={WullingHongGuangMiniEV} title="" alt=""
                      class="img-fluid w-100" />
                    <button type="button" class="btn">VER COLECCIÓN</button>
                  </div>
                </div>
              </div>
              <div class="swiper-slide">
                <div class="row mx-0">
                  <div class="col-12 px-0">
                    <img src={BYDYuanPlus} title="" alt="" class="img-fluid w-100" />
                    <button type="button" class="btn">VER COLECCIÓN</button>
                  </div>
                </div>
              </div>
              <div class="swiper-slide">
                <div class="row mx-0">
                  <div class="col-12 px-0">
                    <img src={CheryeQ1} title="" alt="" class="img-fluid w-100" />
                    <button type="button" class="btn">VER COLECCIÓN</button>
                  </div>
                </div>
              </div>
            </div>
            <div class="swiper-button-next pr-2"></div>
            <div class="swiper-button-prev pl-2"></div>
            <div class="swiper-pagination"></div>
          </div>
        </div>
      </div> */}
    </>
  )
}


export default App
