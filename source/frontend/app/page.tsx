import Link from "next/link";

export default function Home() {
  return (
    <main>
      <section className="bg-white dark:bg-gray-800">
        <div className="container flex flex-col items-center px-4 py-12 mx-auto text-center">
          <h1 className="max-w-2xl mx-auto text-6xl font-semibold tracking-tight text-gray-800 dark:text-white">
            Welcome to <span className="text-indigo-600">ToDo</span>!!
          </h1>

          <p className="max-w-4xl mt-6 text-center text-gray-700 dark:text-gray-400">
            集中する時間、整った生活、心の平穏を、ToDo で手に入れよう。
            <br /> ToDo は ToDo リストアプリです。
          </p>

          <div className="inline-flex w-full mt-6 sm:w-auto">
            <Link
              href="/auth/signup"
              className="inline-block rounded-lg bg-indigo-600 dark: px-4 py-2 text-center text-sm font-semibold text-white outline-none ring-indigo-300 transition duration-100 hover:bg-indigo-500 focus-visible:ring active:bg-indigo-300"
            >
              始める
            </Link>
          </div>
        </div>
      </section>
    </main>
  );
}
