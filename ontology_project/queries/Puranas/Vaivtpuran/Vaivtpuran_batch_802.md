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

### Verse 1 (Vaivtpuran 543.14354)
- **Original**: शरीरको अग्निमें विसर्जित कर दिया। वही दूसरे मुस्कराती हुई बोली। जन्ममें कुब्जा हुई। शूर्पणखाके उकसानेसे शूर्पणखाने कहा--हे राम! हे घनश्याम!
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14355)
- **Original**: मायावी राक्षसराज राबण क्रोधसे काँपने लगा। है रूपधाम! हे गुणसागर! मेरा हृदय आपमें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14356)
- **Original**: उसने मायाद्वारा सीताकों हर लिया। सीताको अनुरक्त हो गया है। आप एकान्त स्थानमें मुझे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14357)
- **Original**: आश्रममें न देख श्रीराम मूच्छित हो गये। तब स्वीकार कीजिये। उनके भाई लक्ष्मणने आध्यात्मिक ज्ञानकी चर्चा तदनन्तर श्रीराम तथा लक्ष्मणसे शूर्पणखाकी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14358)
- **Original**: करके उन्हें सचेत किया। मुने! तत्पश्चात्‌ वे क्र * न हि सत्यात्‌ परो धर्मो नानृतातू पातक॑ परमू ।न हि गज्जासमं तीर्थ न देव: केशवात्‌ पर:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14359)
- **Original**: नास्ति धर्मात्‌ परो अन्धुर्तास्ति धर्मांत्‌ परं धनम्‌ । धर्मात्‌ प्रियः परः को जा स्वधर्म॑ रक्ष यत्नत:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14360)
- **Original**: स्वधमें रक्षिते तात शबश्वत्‌ सर्वत्र मड्लम्‌ । यशस्यं सुप्रतिष्ठा च प्रताप: पूजन॑ परम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14361)
- **Original**: (62। 21-23)
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14362)
- **Original**: 622 ल्‍ संक्षिप्त ब्राह्मवैवर्तपुराण न #####%##########%### कक ऋ$ कक अं कक 494 ##%########%#######&####### यश, प्रतिष्ठा, प्रताप और परम आदरकोी प्राप्ति
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14363)
- **Original**: बातचीत हुई। अन्तमें लक्ष्मणने तीक्ष्ण धारवाले होती है*। मैं चौदह वर्षोतक गृह-सुखका
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14364)
- **Original**: अर्धचन्द्राकार बाणसे उसकी नाक काट ली। परित्याग करके धर्मपूर्वक विचरता हुआ आपके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14365)
- **Original**: उसका भाई खर-दूषण बड़ा बलवान था। उसने सत्यकौ रक्षाके लिये वनमें वास करूँगा। जो
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14366)
- **Original**: आकर युद्ध किया और लक्ष्मणके अस्त्रसे इच्छा या अनिच्छासे सत्य प्रतिज्ञा करके उसका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14367)
- **Original**: सेनासहित मारा जाकर यमलोककों चला गया। पालन नहीं करता, वह अशौचका भागी होता
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14368)
- **Original**: चौदह हजार राक्षसों तथा खर-दूषणको मारा गया है और वह अशौच उसके शरीरके भस्म होनेतक
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14369)
- **Original**: देख शूर्पणखाने रावणको फटकारा और सारा बना रहता है। जबतक चन्द्रमा और सूर्य रहते
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14370)
- **Original**: [समाचार बताकर वह तत्काल पुष्करतीर्थमें चली हैं, तबतक वह कुम्भीपाक नरकमें यातना भोगता
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14371)
- **Original**: गयी। वहाँ दुष्कर तपस्या करके उसने ब्रह्माजीसे है। तदनन्तर मानव-योनिमें उत्पन्न हो वह सात
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14372)
- **Original**: वर प्राप्त किया। उस निराहार-तपस्विनी राक्षसीको जन्मोंतक गूँगा और कोढ़ी होता है। दर्शन देकर सर्वज्ञ कृपासिन्धु ब्रह्माजीने उसके ऐसा कहकर श्रीराम बल्कल और जटा मनकी बात जान ली और इस प्रकार कहा। धारण करके सीता और लक्ष्मणके साथ विशाल
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14373)
- **Original**: ब्रह्माजी बोले--वरानने ! श्रीराम दुर्लभ हैं। वनमें चले गये। मुने! इधर महाराज दशरथने
- **Translation**: 

---

