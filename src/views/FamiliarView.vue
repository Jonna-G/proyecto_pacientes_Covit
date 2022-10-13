<template>
    <div class="signUp_user">
        <div class="container_signUp_user">
            <h2>Familiar</h2>
            <form>
                <input type="text" v-model="fam.id" placeholder="ID">
                <br>
                
                <input type="password" v-model="fam.parentesco" placeholder="Parentesco">
                <br>
                
                <input type="text" v-model="fam.correo" placeholder="Correo">
                <br>

                <input type="email" v-model="fam.iduser" placeholder="IDUSER">
                <br>

                <button type="submit">Registrar</button>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "SignUp",

    data: function(){
        return {
            fam: {
                id: "",
                parentesco: "",
                correo: "",
                iduser: "",
            }
        }
    },

    methods: {
        processSignUp: function(){
            axios.post(
                "http://127.0.0.1:8000/api/familiar/", 
                this.user,  
                {headers: {}}
            )
                .then((result) => {
                    let dataSignUp = {
                        username: this.user.username,
   
                    }
                    
                    this.$emit('completedSignUp', dataSignUp)
                })
                .catch((error) => {
                    console.log(error)
                    alert("ERROR: Fallo en el registro.");  
                });
        }
    }
}
</script>

<style>

    .signUp_user{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
    
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .container_signUp_user {
        border: 3px solid  #283747;
        border-radius: 10px;
        width: 25%;
        height: 60%;
        
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .signUp_user h2{
        color: #283747;

    }

    .signUp_user form{
        width: 70%;
        
    }

    .signUp_user input{
        height: 40px;
        width: 100%;

        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;

        border: 1px solid #283747;
    }

    .signUp_user button{
        width: 100%;
        height: 40px;

        color: #E5E7E9;
        background: #283747;
        border: 1px solid #E5E7E9;

        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0 25px 0;
    }

    .signUp_user button:hover{
        color: #E5E7E9;
        background: crimson;
        border: 1px solid #283747;
    }

</style>