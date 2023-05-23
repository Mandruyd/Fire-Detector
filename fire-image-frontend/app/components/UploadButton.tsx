"use client";

import axios from 'axios';
import React, { ChangeEvent, FormEvent, useState } from 'react';
import ImageComponent from './imageComponent';

const UploadButton = () => {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [uploadedImageUrl, setUploadedImageUrl] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState<boolean>(false);

    const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files[0]) {
            setSelectedFile(event.target.files[0]);
            setUploadedImageUrl(URL.createObjectURL(event.target.files[0]));
        }
    };

    const handleSubmit = async (event: FormEvent) => {
        event.preventDefault();

        if (!selectedFile) 
            return;

        const formData = new FormData();
        formData.append('file', selectedFile);

        setIsLoading(true);

        try {
            const response = await axios.post(`http://${process.env.NEXT_PUBLIC_BACKEND_SERVICE_IP}/detect_fire/`, formData, {
                headers: {"Content-Type": "multipart/form-data"},
                responseType: 'blob',
            });
        
            const imageUrl = URL.createObjectURL(response.data);
            setUploadedImageUrl(imageUrl);
        }
        catch (error) {
            console.log(error);
        } finally {
            setIsLoading(false);
        }        
    };

    return (
        <div>
            <div><ImageComponent imageUrl={uploadedImageUrl} /></div>
            <form onSubmit={handleSubmit}>
                <div className="flex items-center justify-center">
                <div className='py-10'>
                    <input type="file" accept="image/*" onChange={handleFileChange} className='rounded-full'/>
                </div>
                    <button className="bg-teal-100 text-black rounded-full h-12 px-20 text-lg hover:bg-teal-500 hover:scale-105 mr-4" type="submit">Upload</button>
                    {isLoading && 
                        <div className="w-8 h-8 border-t-2 border-b-2 border-teal-500 rounded-full animate-spin"></div>
                    }
                </div>
            </form>
        </div>
    );
};

export default UploadButton;
