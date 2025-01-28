import Image from "next/image";
import Link from "next/link";
import "./globals.css";

export default function Home() {
  return (
    <div className="bg-pink-100 h-[670px]">
      <div className="flex">
        <div>
          <div id="Logo Pinkora">
            <Image
              src="/Pinkora-logo.png"
              alt="Picture of the author"
              width={500}
              height={500}
              className="ml-10"
            />
          </div>
          <div className="ml-16 font-bold">
            <div
              style={{ fontFamily: "Montserrat" }}
              className="flex justify-left  ml-9"
            >
              <p className="text-2xl w-fit">Empowering Early Detection,</p>
            </div>
            <div
              style={{ fontFamily: "Montserrat" }}
              className="flex justify-left  ml-9"
            >
              <p className="text-2xl w-fit">One Prediction at a Time</p>
            </div>
          </div>
        </div>
        <div className="w-[600px]">
          <div
            id="introduction"
            style={{ fontFamily: "Montserrat", fontWeight: "" }}
            className="w-full text-center mt-32"
          >
            Welcome to Pinkora, a revolutionary platform designed to predict
            breast cancer risks using state-of-the-art technology and
            comprehensive data analysis. This application combines machine
            learning algorithms, medical research, and user-friendly features to
            provide you with accurate, personalized insights about your breast
            health.
          </div>
          <div className="pt-5 flex justify-center">
            <Link href="/Form">
            <button>
              <span class="button_top"> Try it Now </span>
            </button>
            </Link>
          </div>
        </div>
      </div>
      <div className="flex justify-center mt-9">
        <div className="flex pointer-curser mr-5 mt-7">
          <Link href="https://github.com/khalid21456/Web-Application-to-Predict-Breast-Cancer-diagnosis">
            <div>
              <Image
                src="/github-logo.png"
                alt="Picture of the author"
                width={30}
                height={30}
                className="ml-2"
                style={{ cursor: "pointer" }}
              />
            </div>
          </Link>
          <Link href="https://www.linkedin.com/in/khalid-edaoudi-8b27a130b/">
            <div>
              <Image
                src="/linkedin-logo.png"
                alt="Picture of the author"
                width={30}
                height={30}
                className="ml-2"
                style={{ cursor: "pointer" }}
              />
            </div>
          </Link>
        </div>
      </div>
    </div>
  );
}
