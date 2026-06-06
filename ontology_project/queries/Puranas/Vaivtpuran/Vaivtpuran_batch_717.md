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

### Verse 1 (Vaivtpuran 543.12654)
- **Original**: (देवल)-से बढ़कर दूसरा कोई मेरा भक्त न तेरा शरीर काजलके समान काला तथा रूप-
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12655)
- **Original**: तो हुआ है और न होगा। त्रह्माजीके प्रपौत्र यौवनसे शून्य हो जाय। आकार अत्यन्त विकृत
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12656)
- **Original**: मुनिवर देवल ऐसे उत्तम तपस्वी थे; परंतु उस तथा तीनों लोकोंमें निन्दित हो और तेरा पुरातन
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12657)
- **Original**: पुंशलीके शापसे उसी तरह हीन अवस्थाको पहुँच तप अवश्य ही शीघ्र नष्ट हो जाय।' गये, जैसे पूर्वकालमें ब्रह्मजी अपूजनीय हो गये यह शाप प्राप्त होनेपर जब मुनिवर देवलने
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12658)
- **Original**: थे। महात्मा देवलका यह सारा गूढ़ रहस्य मैंने आँख खोलकर देखा तो सारा अज्ग विकृत तथा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12659)
- **Original**: कह सुनाया, जो सुखद और पुण्यप्रद है। अब पूर्वपुण्यसे वर्जित दिखायी दिया। तब वे अग्निकुण्ड
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12660)
- **Original**: तुम और क्या सुनना चाहती हो? (अध्याय 30) 3 ्रैँ ै ञ ; कं डे शा त् ई
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12661)
- **Original**: + भ्रीकृष्णजन्मखण्ड * 5
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12662)
- **Original**: 0) 0 ]])]7))4 0
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12663)
- **Original**: 4 44. ख्रह्माजीका मोहिनीके शापसे अपूज्य होना, इस शापके निवारणके लिये उनका वैकुण्ठधाममें जाना और वहाँ अन्यान्य ब्रह्मओंके दर्शनसे उनके अभिमानका दूर होना तदनन्तर श्रीराधिकाने पूछा--श्यामसुन्दर !
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12664)
- **Original**: दयासिन्धु, दीनबन्धु भगवानूसे अपने आगमनका ब्रह्माजीको क्‍यों और किससे शाप प्राप्त हुआ था? रहस्य बताया। वह सारा रहस्य सुनकर भगवान्‌ श्रीकृष्ण बोले--प्रिये! एक बार मोहिनीने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12665)
- **Original**: विष्णु हँसते हुए बोले। ब्रह्माजीसे मिलनकी प्रार्थना की। बहुत समयतक श्रीनारायणने कहा--लोकनाथ! क्षणभर उसका इसके लिये प्रयास चलता रहा; परंतु
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12666)
- **Original**: ठहरो। इसी बीचमें कोई शीघ्रगामी द्वारपाल ब्रह्माजीने उसके उस प्रस्तावकों ठुकरा दिया और
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12667)
- **Original**: श्रीहरिके सामने आया और उन्हें प्रणाम करके एक दिन मुनियोंके सामने मोहिनीका उपहास
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12668)
- **Original**: बोला--' भगवन्‌! दूसरे किसी ब्रह्माण्डके अधिपति किया। इससे मोहिनी कुपित हो उठी और शाप
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12669)
- **Original**: दशमुख ब्रह्मा स्वयं पधारकर द्वारपर खड़े हैं। देती हुई बोली--ब्रह्मन्‌! मैं आपकी दासीके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12670)
- **Original**: वे आपके महान्‌ भक्त हैं और आपका दर्शन समान हूँ, विनयवशील हूँ और दैववश आपकी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12671)
- **Original**: करनेके लिये ही आये हैं।' द्वारपालकी यह बात शरणमें आयी हूँ तो भी आप घमंडमें आकर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12672)
- **Original**: सुनकर भगवान्‌ नाग्यणने उक्त ब्रह्माको भीतर मेरी हँसी उड़ा रहे हैं; अत: सुदीर्घ कालके लिये
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12673)
- **Original**: बुला लानेके लिये उसे अनुमति दे दी। आप अपूजनीय हो जायं। स्वयं भगवान्‌ श्रीहरि
- **Translation**: 

---

