import { gql } from "@apollo/client";
import client from "./api/appollo-client";
import {Image} from 'next/image'


export default function Home({category}) {
  console.log(category)
  
  return (
   <> 
   </>
  )
}
export async function getStaticProps(){

  const {data} = await client.query({
    query:gql`
    query Category{
      category(id:2){
        name
        Products{
          name
          comments{
            body
            createdOn
          }
        }
      }
    }
    `
  });
  return {
    props:{
     
     category:data.category
    }
  }
}

  

