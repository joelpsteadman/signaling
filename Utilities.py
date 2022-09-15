from datetime import datetime

class Formats:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Logger:
    def __init__(self, debug=False):
        self.start_time = datetime.now()
        self.num_issues = 0
        self.show_debugging = debug

    def set_debug(self, debug):
        self.show_debugging = debug

    def _format_mode(self, mode):
        color = None
        if mode == 'DEBUG':
            # mode = '{0: <8}'.format('[' + mode + '] ')
            color = Formats.OKCYAN
        elif mode == 'INFO':
            color = Formats.OKGREEN
        elif mode == 'PROGR':
            color = Formats.OKBLUE
        mode = '{0: <8}'.format('[' + mode + '] ')
        return f'{color}' + mode + f'{Formats.END}'

    def _format(self, args, mode, delimiter=' '):
        delta_time = datetime.now() - self.start_time
        # output = '{0: <16}'.format(''.join('[', mode, ']') + str(delta_time)[0:10]) + ' -'
        mode = self._format_mode(mode)
        output = ''.join(mode + str(delta_time)[0:10]) + ' - '
        for s in args:
            if isinstance(s, str):
                output += s
            else:
                output += str(s)
            output += delimiter
        return output

    def _output(self, args, mode, erase=False, delimiter=' '):
        output = self._format(args, mode=mode, delimiter=delimiter) + '                                '
        if erase:
            print(output, end="\r")
        else:
            print(output)
            # print(f"{Formats.WARNING}Warning: No active frommets remain. Continue?{Formats.END}")

    def info(self, *args, erase=False, delimiter=' '):
        # output = self._format(args, delimiter, mode='INFO') + '                                '
        self._output(args, mode='INFO', erase=erase, delimiter=delimiter)

    def debug(self, *args, erase=False, delimiter=' '):
        if self.show_debugging:
            # output = self._format(args, mode='DEBUG', delimiter=delimiter)
            self._output(args, mode='DEBUG', erase=erase, delimiter=delimiter)

    def display_progress(self, title, interation, max, final = False):
        percent = interation/max
        progress_bar_width = 30
        filled = round(progress_bar_width*percent)
        space = progress_bar_width - filled
        output = title + '█'*filled + ' '*space + str(round(percent*100)) + '%              '
        # output = self._format(''.join(output), delimiter='', mode='PROGR')
        if final:
            self._output(output, mode='PROGR', delimiter='')
        else:
            self._output(output, mode='PROGR', erase=True, delimiter='')

    # def record_csv(self, )