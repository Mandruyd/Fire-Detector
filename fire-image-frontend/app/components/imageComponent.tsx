import React from "react";

const ImageComponent = ({ imageUrl }: { imageUrl: string | null }) => {
    return (
        <div>
            {imageUrl ? (
                <img src={imageUrl} alt="Uploaded" className="w-[640px] h-[640px] bg-fuchsia-800 object-cover rounded-lg py-10 drop-shadow-md" />
            ) : (
                <div className="w-[640px] h-[640px] bg-fuchsia-800 rounded-lg py-10 drop-shadow-md" />
            )}
        </div>
    );
};

export default ImageComponent;
