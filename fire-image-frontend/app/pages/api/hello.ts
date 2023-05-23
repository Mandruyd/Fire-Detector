import { NextApiRequest, NextApiResponse } from "next";

export default function handler(req: NextApiRequest, response:NextApiResponse) {

        response.status(200).json("Hello world!");
}
    