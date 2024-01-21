import Link from "next/link";

export default function SignUp() {
  return (
    <main className="mt-24">
      <div className="flex w-full max-w-sm mx-auto overflow-hidden bg-white rounded-lg shadow-lg dark:bg-gray-800 lg:max-w-4xl">
        <div className="w-full px-6 py-8 md:px-8 lg:w-1/2">
          <div className="flex justify-center mx-auto">
            <svg
              width="95"
              height="94"
              viewBox="0 0 95 94"
              className="h-auto w-6 text-indigo-600"
              fill="currentColor"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M96 0V47L48 94H0V47L48 0H96Z" />
            </svg>
          </div>

          <p className="mt-3 text-xl text-center text-gray-600 dark:text-gray-200">
            サインアップ
          </p>

          <div className="mt-4">
            <label className="block mb-2 text-sm font-medium text-gray-600 dark:text-gray-200">
              Name
            </label>
            <input
              className="block w-full px-4 py-2 text-gray-700 bg-white border rounded-lg dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-indigo-400 focus:ring-opacity-40 focus:outline-none focus:ring focus:ring-indigo-300"
              type="email"
            />
          </div>

          <div className="mt-4">
            <label className="block mb-2 text-sm font-medium text-gray-600 dark:text-gray-200">
              Email Address
            </label>
            <input
              className="block w-full px-4 py-2 text-gray-700 bg-white border rounded-lg dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-indigo-400 focus:ring-opacity-40 focus:outline-none focus:ring focus:ring-indigo-300"
              type="email"
            />
          </div>

          <div className="mt-4">
            <div className="flex justify-between">
              <label className="block mb-2 text-sm font-medium text-gray-600 dark:text-gray-200">
                Password
              </label>
            </div>

            <input
              className="block w-full px-4 py-2 text-gray-700 bg-white border rounded-lg dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-indigo-400 focus:ring-opacity-40 focus:outline-none focus:ring focus:ring-indigo-300"
              type="password"
            />
          </div>

          <div className="mt-4">
            <div className="flex justify-between">
              <label className="block mb-2 text-sm font-medium text-gray-600 dark:text-gray-200">
                Confilm Password
              </label>
            </div>

            <input
              className="block w-full px-4 py-2 text-gray-700 bg-white border rounded-lg dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-indigo-400 focus:ring-opacity-40 focus:outline-none focus:ring focus:ring-indigo-300"
              type="password"
            />
          </div>

          <div className="mt-6">
            <button className="w-full px-6 py-3 text-sm font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-indigo-600 rounded-lg hover:bg-indigo-500 focus:outline-none focus:ring focus:ring-indigo-300 focus:ring-opacity-50">
              サインアップ
            </button>
          </div>

          <div className="flex items-center justify-between mt-4">
            <span className="w-1/5 border-b dark:border-gray-600 md:w-1/4"></span>

            <Link
              href="/auth/signup"
              className="text-xs text-gray-500 dark:text-gray-400 hover:underline"
            >
              or サインイン
            </Link>

            <span className="w-1/5 border-b dark:border-gray-600 md:w-1/4"></span>
          </div>
        </div>
      </div>
    </main>
  );
}
