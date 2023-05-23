import UploadButton from "./components/UploadButton"

export default function Home() {
  return (    
    <div className='bg-gradient-to-br from-purple-500 to-pink-500 min-h-screen grid place-items-center'>
      <h1 className='text-white text-6xl font-bold pb-10 py-10 drop-shadow-md'>Image Fire Detector</h1>
      <div className=''>
        <UploadButton/>
      </div>
    </div>
  )
}
