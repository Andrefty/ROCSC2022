location /vuln {
    content_by_lua_block {
            ngx.req.read_body();
            local arg = ngx.req.get_uri_args();
            for k,v in pairs(arg) do
                    if v == "flag" then
                            ngx.say("This is pwn challange, use power of gods");
                            return -1;
                    end
            end
            ngx.say(arg.id);
            if ngx.var.arg_id == "flag" then
                    file = io.open("/flag", "r");
                    io.input(file);
                    ngx.say(io.read());
                    io.close();
            end
    }
}