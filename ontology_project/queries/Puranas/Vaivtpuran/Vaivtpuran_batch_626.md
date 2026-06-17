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

### Verse 1 (Vaivtpuran 56.5432)
- **Original**: यह समाधि नामक वैश्य है और बड़ा धर्मात्मा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 56.5433)
- **Original**: कृपामयी विष्णुमायाकी सेवा करनेके बाद उन्हें है; तथापि दैववश इसके स्त्री-पुत्रोंने धनके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 56.5434)
- **Original**: सनातन ज्ञानानन्दस्वरूप शिवकी भक्ति प्राप्त होती लोभसे इसको घरसे बाहर निकाल दिया है।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 56.5435)
- **Original**: है। भगवान्‌ शंकर श्रीहरिके ज्ञानके अधिष्ठाता इसका अपराध इतना ही है कि यह स्त्री, पुत्रों देवता हैं। उनका सेवन करके मनुष्य शीघ्र ही और बन्धु-बान्धवोंके मना करनेपर भी प्रतिदिन उनसे श्रीविष्णु-भक्ति प्राप्त कर लेते हैं। तब उनके ब्राह्मणोंको प्रचुर धन और रज्न दानमें दिया करता
- **Translation**: 

---

### Verse 5 (Vaivtpuran 56.5436)
- **Original**: द्वारा सत्त्वस्वरूप सगुण विष्णुकी सेवा होने लगती था। इसीसे क्रोधमें आकर उन लोगोंने इसे घरसे है। इससे उनको परम निर्मल ज्ञानका साक्षात्कार निकाल दिया। फिर शोकके कारण वे पुनः इसका
- **Translation**: 

---

### Verse 6 (Vaivtpuran 56.5437)
- **Original**: होता है। सगुण विष्णुकी आराधनाके पश्चात्‌ अन्वेषण करते हुए आये। परंतु यह पवित्र, ज्ञानी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 56.5438)
- **Original**: सात्त्विक वैष्णव मानव प्रकृतिसे परवर्ती निर्गुण एवं विरक्त वैश्य उनके आग्रह करनेपर भी घरको
- **Translation**: 

---

### Verse 8 (Vaivtpuran 56.5439)
- **Original**: श्रीकृष्णकी भक्ति पाते हैं। तदनन्तर वे साधु पुरुष नहीं लौटा। तब इसके पुत्र भी पितृशोकसे संतस्त
- **Translation**: 

---

### Verse 9 (Vaivtpuran 56.5440)
- **Original**: श्रीकृष्णके निरामय मन्त्रको ग्रहण करते हैं और हो सब कर्मोंसे विरक्त हो गये और सारा धन
- **Translation**: 

---

### Verse 10 (Vaivtpuran 56.5441)
- **Original**: उन निर्गुण देवकी आराधनासे स्वयं निर्गुण हो ब्राह्मणॉंकों देकर घर छोड़ बनको चले गये।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 56.5442)
- **Original**: जाते हैं। वे वैष्णव पुरुष निरामय गोलोकमें “श्रीहरिका परम दुर्लभ दास्य प्राप्त हो '--यही इस
- **Translation**: 

---

### Verse 12 (Vaivtpuran 56.5443)
- **Original**: रहकर निरन्तर भगवान्‌का दास्य-(कैंकर्य-)मय वैश्यका अभीष्ट मनोरथ है। इस निष्काम वैश्यको
- **Translation**: 

---

### Verse 13 (Vaivtpuran 56.5444)
- **Original**: सेवन करते हैं और अपनी आँखोंसे अगणित वह अभीष्ट वस्तु कैसे प्राप्त होगी ? यह बात आप
- **Translation**: 

---

### Verse 14 (Vaivtpuran 56.5445)
- **Original**: ब्रह्माओंका पतन (विनाश) देखते हैं। जो श्रेष्ठ विस्तारपूर्वक बतानेकी कृपा करें। मानव श्रीकृष्णभक्तसे उनके मन्त्रकी दीक्षा ग्रहण श्रीमेधसने कहा--राजन्‌! निर्गुण परमात्मा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 56.5446)
- **Original**: करता है, वह अपने पूर्वजोंकी सहस्नरों पीढ़ियोंका श्रीकृष्णकी आज्ञासे दुर्लह्ब्य त्रिगुणमयी विष्णुमाया
- **Translation**: 

---

### Verse 16 (Vaivtpuran 56.5447)
- **Original**: उद्धार कर देता है। इतना ही नहीं, बह नानाके सम्पूर्ण विश्वकों अपनी मायासे आच्छन्न कर देती
- **Translation**: 

---

### Verse 17 (Vaivtpuran 56.5448)
- **Original**: कुलकी सहस्रों पीढ़ियोंका, माताका तथा दास है। वह कृपामयी देवी जिन धर्मात्मा पुरुषोंपर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 56.5449)
- **Original**: आदिका भी उद्धार करके गोलोकमें चला जाता कृपा करती है, उन्हें दया करके परम दुर्लभ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 56.5450)
- **Original**: है। महाभयंकर भवसागरमें कर्णधाररूपिणी दुर्गा श्रीकृष्ण-भक्ति प्रदान करती है। नरेश्वर! परंतु
- **Translation**: 

---

### Verse 20 (Vaivtpuran 56.5451)
- **Original**: श्रीकृष्ण-भक्तिरूपी नौकाद्वारा उन सबको पार कर जिन मायावी पुरुषोंपर विष्णुमाया दया नहीं करती
- **Translation**: 

---

