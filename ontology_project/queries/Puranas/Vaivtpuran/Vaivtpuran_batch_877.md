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

### Verse 1 (Vaivtpuran 543.15854)
- **Original**: जिसका स्तवन स्वयं ब्रह्मा और सनातन भगवान्‌ गड्जा, तुलसी, स्वाहा, स्थधा और सती हो। विष्णु नहो-ं कर सकते, उसकी स्तुति युद्धसे समस्त देवाड्नाएँ तुम्हारे अंशांशकी अंशकलासे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15855)
- **Original**: भयभीत हुआ मैं अपने पाँच मुखोंद्वारा कैसे कर उत्पन्न हुई हैं। देवि! स्त्री, पुरुष और नपुंसक तुम्होर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15856)
- **Original**: सकता हूँ? अतः महामाये! तुम मुझपर कृपा ही रूप हैं। तुम वुक्षोंमें वृक्षरूपा हो और अंकुर-रूपसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15857)
- **Original**: करके मेरे शत्रुका बरिनाश कर दो। करुणासहित तुम्हाा सृजन हुआ है। तुम अग्निमें दाहिका शक्ति,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15858)
- **Original**: यों कहकर रणक्षेत्रमें शिवजीके रथपर गिर जानेपर जलमें शीतलता, सूर्यमें सदा तेज:स्वरूप तथा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15859)
- **Original**: करोड़ों सूर्योके समान कान्तिमती दुर्गा प्रकट हो कान्तिरूप, पृथ्वीमें गन्धरूप, आकाशमें शब्दरूप,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15860)
- **Original**: गयीं। उस समय परमात्मा नारायणने कृपापरवश चन्द्रमा और कमलसमूहमें सदा शोभारूप, सृष्टिमें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15861)
- **Original**: हो उन्हें प्रेरित किया था। तब वे महादेवी शीघ्र 2:302:7:7% 020 पालन-कार्यमें भलीभाँति पालन
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15862)
- **Original**: ही शिवके समक्ष खड़ी हो उनके मड्गल और करनेबाली, संहारकालमें महामारी और जलमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15863)
- **Original**: विजबके लिये यों बोलीं-- “शिव! मायाशक्तिका जलरूपसे वर्तमान रहती हो। तुम्हीं श्षुधा, तुम्हीं
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15864)
- **Original**: आश्रय लेकर असुरका संहार करो*।' * श्रीमहादेव उत्ाच-- रक्ष रक्ष महादेवि दुर्गे दुर्गतिनाशिति
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15865)
- **Original**: मां भक्तमनुरक्त॑ च॑ शत्रुग्रस्त॑ कृपामयि
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15866)
- **Original**: विष्णुमाये. महाभागे. नारायण समातति । ब्रह्मस्वरूपे परमे नित्यानन्दस्वरूपिणि
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15867)
- **Original**: त्व॑ च. ब्रह्मादिदेवानामम्येकि जगदम्बिके । त्य॑ साकोरे च गुणतो निराकारे च निगुंणात्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15868)
- **Original**: मायया पुरुषस्त्व॑ च. मायया प्रकृति: स्वयम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15869)
- **Original**: तयो: पर ब्रह्म परं त्वं बिरभर्षि सनातनि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15870)
- **Original**: वेदानां जननी त्य॑ च सावित्री च परात्परा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15871)
- **Original**: वैकुण्ठे च महालक्ष्मी: सर्वसम्पत्स्वरूपिणी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15872)
- **Original**: मर्त्यलक्ष्मीक क्षीरोदे कामिनी. शेषशायिनः । स्वर्गेषु. स्वर्गलक्ष्मीस्त्व॑ राजलक्ष्मीक्ष भूठले
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15873)
- **Original**: नागादिलक्ष्मों:3.. पाताले गृहेषपु. गृहदेवता । सर्वशस्यस्वरूपा._त्व॑ सर्वैश्चर्यविधायिनी
- **Translation**: 

---

