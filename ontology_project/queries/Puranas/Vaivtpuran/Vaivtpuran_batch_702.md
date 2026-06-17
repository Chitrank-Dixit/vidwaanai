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

### Verse 1 (Vaivtpuran 295.18156)
- **Original**: सर्वसय्पत्प्रदात्रीं च महालक्ष्मी भजे शुभाम्‌। (प्रकृतिखण्ड 39
- **Translation**: 

---

### Verse 2 (Vaivtpuran 295.18157)
- **Original**: 10--12-) लक्ष्म्या मन्त्र: लक्ष्मीमायाकामवाणी ततः कमलवासिनी । स्वाहान्तो बैदिको मन्त्रराजो5यं द्वादशाक्षर:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 295.18158)
- **Original**: कुबेरोड-नेन मन्त्रेण . सर्वैश्वर्यमवाप्तवान्‌ । राजराजेश्ररो दक्ष: सावर्णिम्मनुरेव च
- **Translation**: 

---

### Verse 4 (Vaivtpuran 295.18159)
- **Original**: मड्लोडइनेन मन्त्रेण. साप्ठीपवतीपतिः । प्रियक्गतोत्तानपादा केदारो नृूष एवं चा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 295.18160)
- **Original**: एते च सिद्धा राजेन्द्रा मन््रेणानेन मारद। (प्रकृतिखण्ड 39। 43-453)
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12359)
- **Original**: * भ्रीकृष्णजन्मखण्ड 543 444 4204 8 4 2 40 2 8
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12360)
- **Original**: ) )]2) 8) /]]][27]7]
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12361)
- **Original**: [[।।।।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12362)
- **Original**: । 2 आप उन्हें बीज और फल दोनों प्रदान करती
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12363)
- **Original**: साथ थीं। सिंहसे जुते हुए रथपर बैठी तथा रत्नमय हैं, कोई भी आपका निर्वचन (निरूपण) नहीं कर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12364)
- **Original**: अलंकारोंसे विभूषित थीं। उनके दस भुजाएँ थीं। सकता है, महामाये ! आपको नमस्कार है। शिवे !
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12365)
- **Original**: उन्होंने रल्सारमय उपकरणोंसे युक्त सुवर्णनिर्मित आप शंकरसम्बन्धी सौभाग्यसे सम्पन्न हैं तथा दिव्य रथसे उतरकर तुरंत ही श्रीराधाकों हृदयसे सबको सौभाग्य देनेवाली हैं। देवि! श्रीहरि ही मेरे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12366)
- **Original**: लगा लिया। देवी दुर्गाको देखकर अन्य गोपकुमारियोंने प्राणवल्लम और सौभाग्य हैं; उन्हें मुझे दीजिये।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12367)
- **Original**: भी प्रसन्नतापूर्वक प्रणाम किया। दुर्गाने उन्हें आपको नमस्कार है। जो स्त्रियाँ ब्रतकी समाप्तिके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12368)
- **Original**: आशीर्वाद देते हुए कहा-“तुम सबका मनोरथ दिन इस स्तोत्रसे शिवादेवीकी स्तुति करके बड़ी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12369)
- **Original**: सिद्ध होगा।' इस प्रकार गोपिकाओंको वर दे भक्तिसे उन्हें मस्तक झुकाती हैं; वे साक्षात्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12370)
- **Original**: उनसे सादर सम्भाषण कर देवीने मुस्कराते हुए श्रीहरिको पतिरूपमें प्राप्त करती हैं। इस लोकमें - परात्पर परमे श्वरको पतिरूपमें पाकर कान्त-सुखका उपभोग करके अन्तमें दिव्य विमानपर आरूढ़ हो भगवान्‌ श्रीकृष्णके समीप चली जाती हैं*। समाप्तिके दिन गोपियोंसहित श्रीराधाने देवीकी बन्दना और स्तुति करके गौरीब्रतको पूर्ण किया। घर जानेको उद्यत हुईं। उन्होंने आदरपूर्वक एक हजार ब्राह्मणोंकों भोजन कराया, बाजे बजबाये और भिखमंगोंको धन बाँटा। इसी समय दुर्गतिनाशिनी दुर्गा वहाँ आकाशसे प्रकट हुईं, जो ब्रह्मतेजसे प्रकाशित हो रही थीं। उनके प्रसन्न मुखपर मन्द हास्यकी प्रभा फैल रही थी। वे सौ योगिनियोंके *जानक्युवाच-- शक्तिस्वरूपे.. सर्वेषां सर्वाधारे गुणाश्रये
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12371)
- **Original**: सदा शंकरयुक्ते च पतिं देहि नमो5स्तु ते
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12372)
- **Original**: सृष्टिस्थित्यन्तरूपेण सृष्टिस्थित्यन्तरूपिणि । सृष्टिस्थित्यन्तबीजानां बौजरूपे नमो5स्तु ते
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12373)
- **Original**: हे गौरि पतिमर्मक्षे पतिब्रतपरायणे । पतित्रते पतिरते पति देहि नमो5स्तु ते
- **Translation**: 

---

