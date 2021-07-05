from .. import loader, utils

@loader.tds
class RPMod(loader.Module):
    """Модуль RPMod"""
    strings = {'name': 'RPMod'}

    async def client_ready(self, client, db):
        self.db = db
        self.db.set("RPMod", "status", True)

    async def rpmodcmd(self, message):
        """Используй: .rpmod чтобы включить/выключить RP режим."""
        status = self.db.get("RPMod", "status")
        if status is not False:
            self.db.set("RPMod", "status", False)
            await message.edit("<b>RP Режим <code>выключен</code></b>")
        else:
            self.db.set("RPMod", "status", True)
            await message.edit("<b>RP Режим <code>включен</code></b>")

    async def rplistcmd(self, message):
        """Используй: .rplist чтобы посмотреть список рп команд."""
        await message.edit("<b> • чмок\n • чпок\n • кусь\n • обнять\n • шлеп\n • убить\n • выебать\n • связать\n • ударить\n • уебать\n • отсосать\n • отлизать\n • задушить\n • украсть"
                           "\n • погладить\n • притянуть\n • изнасиловать\n • отпороть\n • наебать\n • поцеловать\n • накурить\n • набухать\n • засосать\n • утопить\n"
                           " • расстрелять\n • прижать\n • понюхать\n • отдаться\n • покормить\n • кастрировать\n • пнуть\n • пожелать спокойной ночи\n • лизнуть\n"
                           " • послать нахуй\n • ущипнуть\n • дать чапалаха\n • полюбить\n • признаться в любви\n • трахнуть\n • заебать\n • доебаться\n • дать бан\n"
                           " • принудить\n • отшлепать\n • разозлил(а)\n • торт\n • кинуть камень\n • выкинуть\n • закопать\n • выкопать\n • запопать\n"
                            " • сосать\n • отлизать\n • выебать\n • пожениться\n • уложить\n • ❤️\n • рука и сердце\n • кинуть на карту\n • купить еду\n • купить пиво\n • выпить пиво\n</b>")

    async def watcher(self, message):
        try:
            status = self.db.get("RPMod", "status")
            reply = await message.get_reply_message()
            user = await message.client.get_entity(reply.sender_id)
            me = (await message.client.get_me())
            if status is not False:
                if message.sender_id == me.id:
                    if message.text.lower() == "чмок":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> чмокнул <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "чпок":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> чпокнул <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "кусь":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кусьнул <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "обнять":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> обнял <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "шлеп":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> шлепнул <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "убить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> убил <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "выебать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> выебал <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "связать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> связал <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "ударить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> ударил <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "уебать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> уебал <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отсосать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отсосал у <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отлизать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отлизал у <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "задушить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> задушил <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "украсть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> украл <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "погладить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> погладил <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "притянуть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> притянул <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "изнасиловать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> изнасиловал <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    if message.text.lower() == "отпороть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отпорол <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "наебать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> наебал <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "поцеловать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> поцеловал <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "накурить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> накурил <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "набухать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> залил в горло <a href=tg://user?id={user.id}>{user.first_name}</a> литр водки")

                    if message.text.lower() == "засосать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> засосал <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "утопить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> утопил <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "расстрелять":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> расстрелял <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "прижать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> прижал к стене <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "понюхать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> понюхал <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "отдаться":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отдался <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "покормить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> покормил <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "кастрировать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> орезал бубенчики <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "пнуть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> пнул <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "пожелать спокойной ночи":
                        await message.edit(f"Спокойной ночи <a href=tg://user?id={user.id}>пидор</a>")

                    if message.text.lower() == "послать нахуй":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> послал нахуй <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "лизнуть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> лизнул <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "ущипнуть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> ущипнул <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    
                    if message.text.lower() == "дать чапалаха":
                        await message.edit(f"<a href=tg://user?id={user.id}>{user.first_name}</a> получил чапалах со скоростью света от <a href=tg://user?id={me.id}>{me.first_name}</a>")
                    
                    if message.text.lower() == "полюбить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> полюбил <a href=tg://user?id={user.id}>{user.first_name}</a>")
                        
                    if message.text.lower() == "признаться в любви":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> признался в любви <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "трахнуть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> трахнул <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "заебать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> заебал <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "доебаться":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> доебался <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "дать бан":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> забанил <a href=tg://user?id={user.id}>{user.first_name}</a>")
                    
                    if message.text.lower() == "принудить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> принудил <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "отшлепать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> отшлепал <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "разозлила":
                        await message.edit(f"<a href=tg://user?id={user.id}>{user.first_name}</a> разозлила <a href=tg://user?id={me.id}>{me.first_name}</a>")

                    if message.text.lower() == "разозлил":
                        await message.edit(f"<a href=tg://user?id={user.id}>{user.first_name}</a> разозлил <a href=tg://user?id={me.id}>{me.first_name}</a>")    

                    if message.text.lower() == "сосать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> заставил себе сосать <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "торт":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> подарил торт <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "кинуть камень":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кинул камнем у <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "выкинуть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> выкинул <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "закопать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> закопал <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "выкопать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> выкопал <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "запопать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> запопил <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "пожениться":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> поженился с <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "уложить спать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> уложил спать <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "❤️":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> подарил свое ❤ <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "рука и сердце":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> подарил руку и свое сердце <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "кинуть на карту":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кинул деньги на карту <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "купить еду":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> купил еду <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "купить пиво":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> купил пиво <a href=tg://user?id={user.id}>{user.first_name}</a>")

                    if message.text.lower() == "выпить пиво":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> выпил пиво с <a href=tg://user?id={user.id}>{user.first_name}</a>")












                        

    

























                    
        except: pass