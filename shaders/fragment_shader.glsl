#version 430

uniform vec2 resolution;
uniform float time;

out vec4 fragColour;

void main() {
    // Maintain aspect ratio, regardless of canvas dimensions
    vec2 uv = (gl_FragCoord.xy * 2.0 - resolution.xy) / resolution.y;

    float d = length(uv);
    vec3 col = vec3(d);

    fragColour = vec4(col, 1.0);
}
