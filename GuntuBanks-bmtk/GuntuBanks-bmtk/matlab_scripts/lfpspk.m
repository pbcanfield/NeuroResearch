function [data] = lfpspk(h5path, network, nfft, noverlap)
% LFP takes an h5 ecp file output from bmtk and a channel number
% Plots severla plots for frequency power USING PSAUTOSPK.m
% Example usage:
% lfp('../100_output/spikes.h5','hippocampus');

node_id_path = join(['/spikes/',network,'/node_ids']);
timestamp_path = join(['/spikes/',network,'/timestamps']);

node_ids = h5read(h5path,node_id_path);
timestamps = h5read(h5path,timestamp_path);

% assuming LFP is stored in an array called LFP
fs = 10000; % sampling frequency in Hz
dt = .1; % delta time
sp = 1/dt; %samples per
p = fs*sp; %total bins where spike is possible (total timesteps)
spk = zeros(1,p); %array of zeros, one for each timestep
s = int64(timestamps*sp); %change timestamps of spikes to indices
spk(s) = 1; %set spike times

if ( nargin == 2 )
  nfft = 1024;
  noverlap = 512;
end;

if ( nargin == 3 )
  noverlap = 512;
end;


%psautospk(spk,dt,nfft)
window = hanning(1024);
psautospk(spk,dt,nfft,window,noverlap);

end

