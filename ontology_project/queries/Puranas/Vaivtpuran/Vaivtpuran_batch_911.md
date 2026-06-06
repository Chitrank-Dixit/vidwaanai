# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vaivtpuran 543.16534)
- **Original**: ककुझी अमूल्य रत्नोंके सारसे निर्मित रथद्वाग़ महाबली राजा ककुझी अपनी कन्याके लिये वरकी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16535)
- **Original**: कुण्डि-नगरकों गये। तदनन्तर उस वैवाहिक तलाशमें ब्रह्मलोकसे भूतलपर आये। उनकी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16536)
- **Original**: मद्जगल-कार्यके समाप्त होनेपर देवकौ, रोहिणी, कन्याका नाम रेवती था। वह निरन्तर स्थिर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16537)
- **Original**: नन्‍्दपत्री यशोदा, अदिति, दिति और शान्तिने यौवनवाली, अमूल्य रत्नोंसे विभूषित और तीनों
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16538)
- **Original**: जय-जयकार करके रेबतीको, जो नारियोंमें श्रेष्ठ लोकोंमें दुर्लभ थी। उसकी आयुके सत्ताईस युग
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16539)
- **Original**: तथा लक्ष्मीकी कलास्वरूपा थीं, महलमें प्रवेश बोत चुके थे। राजाने कौतुकवश अपनी उस
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16540)
- **Original**: कराया। तत्पश्चात्‌ वसुदेवजीकी प्रियतमा पत्नी कन्याको महाबली बलदेवकों ब्याह दिया। इस देवकोने हर्षपूर्बवक सारा मड्गल-कार्य सम्पन्न प्रकार मुनियों तथा देवेन्द्रोंकी सभामें विधानपूर्वक
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16541)
- **Original**: कराया और ब्राह्मणोंकों भोजन कराकर उन्हें धन कन्यादान करके राजाने लाखों-लाखों हाथी, [दान दिया। घोड़े, रथ, रत्नाभूषण, मणि-रत्न, करोड़ों स्वर्णमुद्रां.. तदनन्तर देवताओं और मुनियोंका समुदाय जामाताको दहेजमें दीं तथा सुन्दर दिव्य वस्त्रादि
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16542)
- **Original**: तथा देश-देशान्तरके नरेश आनन्दमग्र हो अपनी- दिये । यों बलशाली बलदेवको कन्या देकर राजेन्द्र अपनी सेनाओंके साथ सहसा कुण्डिन-नगरमें आ
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16543)
- **Original**: जरधाबा हक्ाकक बता ध्रकलाकभ कल बता त्रकतात 2तंतकीमाा बचत का आन बाल कब घर बत का कत तल 8 20 प रत 0 कत शा बह पहुँचे। उन सब लोगोंने उस परम मनोहर नगरका
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16544)
- **Original**: दुष्कर तथा मुनीन्‍्द्रों, देवगणों और मुनिवरोंके अवलोकन किया। बारातियोंने उस नगरके बाहरी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16545)
- **Original**: लिये उपहासास्पद थे। दरवाजेको देखा; चार महारथी सैनिकोंके साथ रुक्मिने कहा--अहो ! कालकृत कर्म और उसकी रक्षा कर रहे थे। उनके नाम थे-रुक्मी,
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16546)
- **Original**: दैवकों कौन हटा सकता है? भला, मैं देवेद्रोंकी शिशुपाल, महाबली दन्तवक्र और मायावियोंमें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16547)
- **Original**: सभामें क्या कहूँगा; क्योंकि जो नन्‍्दके पशुओंका श्रेष्ठ एवं युद्ध-शास्त्रमें निण शाल्ब। उस समय
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16548)
- **Original**: रखवाला, गोपियोंका साक्षात्‌ लम्पट और ग्वालोंकी राजकुमार रुक्मि, जो युद्धके लिये उद्यत हो नाना
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16549)
- **Original**: जूँठन खानेवाला है तथा जिसकी जाति, खान- शस्त्रास्त्रोंसे सुसज्जित रथपर सवार था, श्रीकृष्णकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16550)
- **Original**: पान और उत्पत्तिका कोई निर्णय ही नहीं है; यह सेनाका अवलोकन करके कुपित हो उठा और
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16551)
- **Original**: भी पता नहीं कि क्या वह राजकुमार है अथवा किसी मुनिका पुत्र है; जिसके पिता वसुदेव क्षत्रिय , -/
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16552)
- **Original**: हैं, परंतु जिसका भरण-पोषण वैश्यके घर हुआ <5
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16553)
- **Original**: है; जिस दुष्टने अभी हालमें हो मथुरामें धर्मात्मा $ रद (
- **Translation**: 

---

