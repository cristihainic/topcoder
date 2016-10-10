class DiskSpace:

    def minDrives(self, used, total):

        total_memory_needed = 0
        drives_needed = 0

        for i in used:
            total_memory_needed += i

        for i in sorted(total, reverse=True):
            if total_memory_needed > 0:
                total_memory_needed -= i
                drives_needed += 1

        return drives_needed
