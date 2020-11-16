using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using System.IO;
using Newtonsoft.Json;
using System.Web;

namespace LibTXNDCCSharp
{
    /// <summary>
    /// This class 
    /// </summary>
    static class NDCLauncher
    {
        static string _pythonPath = "python.exe";
        static string _libTXNDCPyPath = ".\\..\\..\\..\\LibTXNDCPy\\LibTXNDCPy";

        /// <summary>
        /// Launches LibTXNDCPy's command line entry point from within a .NET application.
        /// </summary>
        /// <param name="samples">Populated LibTXNDCCSharp samples object</param>
        /// <returns>XML representation of the samples object, as a string</returns>
        public static string launchConvertSamples(NDCSamples samples)
        {
            string ret = null;

            string jsonContent = JsonConvert.SerializeObject(samples);

            string args = _libTXNDCPyPath + "\\NDCconvertSamples.py -u -d " + System.Web.HttpUtility.UrlEncode(jsonContent);

            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = _pythonPath;
            start.Arguments = string.Format("{0}", args);
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            start.RedirectStandardError = true;

            var process = new Process();
            process.StartInfo = start;
            process.Start();

            var output = new List<string>();

            while (process.StandardOutput.Peek() > -1)
            {
                output.Add(process.StandardOutput.ReadLine());
            }

            while (process.StandardError.Peek() > -1)
            {
                output.Add(process.StandardError.ReadLine());
            }
            
            process.WaitForExit();

            ret = string.Empty;

            foreach(string line in output)
            {
                ret += line;
            }

            ret = System.Web.HttpUtility.UrlDecode(ret);

            return ret;
        }

        /// <summary>
        /// This is the path to the Python executable to use for launching LibTXNDCPy
        /// </summary>
        public static string PythonPath
        {
            get
            {
                return _pythonPath;
            }

            set
            {
                _pythonPath = value;
            }
        }

        /// <summary>
        /// This is the path to the LibTXNDCPy python files
        /// </summary>
        public static string LibTXNDCPyPath
        {
            get
            {
                return _libTXNDCPyPath;
            }

            set
            {
                _libTXNDCPyPath = value;
            }
        }

    }
}
