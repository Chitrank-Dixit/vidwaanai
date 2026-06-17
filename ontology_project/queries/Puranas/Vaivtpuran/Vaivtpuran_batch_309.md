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

### Verse 1 (Vaivtpuran 13.12322)
- **Original**: दस्युभूत राक्षस्रोंका नाश करनेके लिये पूर्ण क्योंकि आप संदेहका निवारण करनेवाले हैं। परमात्मा विष्णु दशरथनन्दन श्रीरामके रूपमें भगवान्‌ श्रीनारायणने कहा--नारद!
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.12323)
- **Original**: वसुधापर पधारेंगे। उनके दो भक्त जय और कुशध्वजकी पुत्री सती वेदवतीने महान्‌ तीर्थ
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.12324)
- **Original**: बिजय ब्राह्मणोंक शापके कारण वैकुण्ठधामसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.12325)
- **Original**: पडर + संक्षिप्त ग्रह्नवैयर्तपुराण कि 47]7774+4+74+4+4]]]
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.12326)
- **Original**: 4।।।।।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.12327)
- **Original**: । । 8] 3] 3] 8 82) ॉ0
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.12328)
- **Original**: 4 8 3. नीचे गिर गये हैं। उनका उद्धार करनेके लिये
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.12329)
- **Original**: पतिकी प्राप्ति होती है, इसमें संशय नहीं है। त्रेतायुगमें अवोध्यापुरीके भीतर श्रीहरिका आविर्भाव
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.12330)
- **Original**: भगवान्‌ नारायण कहते हैं--इस प्रकार होगा। तुम भी शिशुरूप धारण करके मिथिलाको
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.12331)
- **Original**: उन गोपकुमारियोंने एक मासतक ब्रत किया। वे जाओ। वहाँ राजा जनक अयोनिजा कन्याके [ पूर्वोक्त स्तोत्रसे प्रतिदिन देवीकी स्तुति करती थीं। रूपमें तुम्हें पाकर॑ यत्रपूर्वक तुम्हाशा लालन-पालन
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.12332)
- **Original**: समाप्तिके दिन ब्रत पूर्ण करके गोपियॉंकों बड़ी करेंगे। वहाँ तुम्हारा नाम सीता होगा। श्रीराम
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.12333)
- **Original**: प्रसन्नता हुई। उन्होंने काण्व-शाखामें वर्णित उस भी मिथिलामें जाकर तुम्हारे साथ विवाह करेंगे। स्तोन्नद्वारा परमेश्वर पार्वतीका स्तवन किया, तुम प्रत्येक कल्पमें नारायणकी ही प्राणवल्लभा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.12334)
- **Original**: जिसके द्वारा स्तुति करके सत्यपरायणा सीताने होओगी। शीघ्र ही कमल-नयन श्रीरामको प्रियतम पतिके यों कह पार्वती वेदबतीको इृदयसे लगाकर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.12335)
- **Original**: रूपमें प्राप्त किया था। बह स्तोत्र यह है। अपने निवास-स्थानको लौट गयीं। साध्वी वेदवती
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.12336)
- **Original**: जानकी बोलीं--सबकी शक्तिस्वरूपे ! शिवे ! मिथिलामें जाकर मायासे हलद्वारा भूमिपर की
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.12337)
- **Original**: आप सम्पूर्ण जगत्‌की आधारभूता हैं। समस्त गयी रेखा (हराई)-में सुखपूर्वक स्थित हो गयीं।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.12338)
- **Original**: सदु्णोंकी निधि हैं तथा सदा भगवान्‌ शंकरके उस समय राजा जनकने देखा, एक नग्न बालिका
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.12339)
- **Original**: संयोग-सुखका अनुभव करनेवाली हैं; आपको आँख बंद किये भूमिपर पड़ी है। उसकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.12340)
- **Original**: नमस्कार है। आप मुझे सर्वश्रेष्ठ पति दीजिये। सृष्टि, अन्जकान्ति तपाये हुए सुवर्णके समान उद्दी्र है
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.12341)
- **Original**: पालन और संहार आपका रूप है। आप सृष्टि, तथा वह तेजस्विनी बालिका रो रही है। उसे [पालन और संहाररूपिणी हैं। सृष्टि, पालन और देखते ही राजाने उठाकर गोदमें चिपका लिया।
- **Translation**: 

---

