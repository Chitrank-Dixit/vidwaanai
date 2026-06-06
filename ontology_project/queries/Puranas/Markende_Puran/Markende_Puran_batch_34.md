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

### Verse 1 (Markende Puran 0.661)
- **Original**: चाहिये; क्योंकि स्त्रोके लिये पति हो परम गति पूछनेपर उन्होंने अपनी, अपने स्वामीकी तथा
- **Translation**: 

---

### Verse 2 (Markende Puran 0.662)
- **Original**: हैं। पति जो देवताओं, पितरों तथा अतिधियोंकी कक लक >> नसक -+- आओ. यनगनभगभगभगसऋो_ _..3 आओ. कस तस्मात्‌ पतिक्नतात्रेश्सू्सा तपर्रिकनोंगू। प्रसादयह थे पतली भानोरुदबकाम्ध्मा
- **Translation**: 

---

### Verse 3 (Markende Puran 0.663)
- **Original**: (16। 48 49) अनसूवोष'च
- **Translation**: 

---

### Verse 4 (Markende Puran 0.664)
- **Original**: पतिब्रताणा पाहाकय व ड्ीयेत कर्थ स्वित। सागान्य रुख्थात्‌ त॑ साध्यौमठः रक्ष्यास्थर सुरा:
- **Translation**: 

---

### Verse 5 (Markende Puran 0.665)
- **Original**: यथा पुनरहोराजलंस्थानमुपजाफी . सथा ये तध्वा: स्वपतिर्त साया गारमे'्यति
- **Translation**: 

---

### Verse 6 (Markende Puran 0.666)
- **Original**: (16। 51-72) ऊजिन्रन्ड/ए कल्याए स्वभतुर्मुजदर्शात्‌। कन्बिच्याखिलदेजेभ्पो मजसे4भयधरफ़॑पतिस्‌
- **Translation**: 

---

### Verse 7 (Markende Puran 0.667)
- **Original**: भवृशुश्रूपगादेय सपा आधे महव्‌ फलम्‌। स्वकानफ़ल्यवाप्या. प्रत्यूदा: पॉटबर्तिया:
- **Translation**: 

---

### Verse 8 (Markende Puran 0.668)
- **Original**: 54-59)
- **Translation**: 

---

### Verse 9 (Markende Puran 0.669)
- **Original**: डे +संक्षिप्त सार्कण्जेय पुराण+ -- 37%%846:::3:20 074 फ्रऋरा///भद 4 #43+55784
- **Translation**: 

---

### Verse 10 (Markende Puran 0.670)
- **Original**: 55205645527/746442310 077
- **Translation**: 

---

### Verse 11 (Markende Puran 0.671)
- **Original**: ध20 057 रू धार ]0 8522 फणण रथ मे पसत्कारपुर्वक 5जा ऋरता है, उसके भो पुण्यका. अनसूबा बोलीं--देजि ! तुम्हारे लचनसे दिन- आधा भाग स्त्री अनन्यन्तसे पत्तिकी सेवा करेमात्रसे
- **Translation**: 

---

### Verse 12 (Markende Puran 0.672)
- **Original**: रातको व्यवस्थाका लोप हो जानेके कारण सुभ प्रा कर लेहीं तै।* कर्मौका अनुष्ठान घंद हो गया है; इसलिये ये अनसुदाजीका चचन सुनकर पतिव्रता क्राह्मणीने इन्द्र आदि देवता मेंरे पास दुखी होकर आये हैं चढ्ट आदरके साथ टनका पूजन किया और इस
- **Translation**: 

---

### Verse 13 (Markende Puran 0.673)
- **Original**: और प्रार्थना करते हैं कि दिन-रातकौ व्यत्नस्था प्रकार कहा--' स्व भावत: सबका कल्याण ऋरतेवाली
- **Translation**: 

---

### Verse 14 (Markende Puran 0.674)
- **Original**: पहलेकी-त्तरह अखण्डरूपसे चलती रहे। में देवों! रबयं॑ आप यहाँ पधारकर पत्तिकौ सेवामें
- **Translation**: 

---

### Verse 15 (Markende Puran 0.675)
- **Original**: इसीक्रे लिये तुम्हारे पास आयी हूँ। मेरी यह जात भेरों पर: श्रद्धा बब्य रही हैं। इससे में धन्य हो सुनों। दिन न होनेसे सपस्त अज्ञकपोंक्या अधात्र गयों। यह आपका मुझपर यहुत बड़ा अनुप्रह है।
- **Translation**: 

---

### Verse 16 (Markende Puran 0.676)
- **Original**: हो गया है और यज्ञेकि अभावसे देवताओंक्ी पुष्टि इसीसे देवताओंने भी
- **Translation**: 

---

### Verse 17 (Markende Puran 0.677)
- **Original**: ज मुझपर क्ृपादृष्टि को
- **Translation**: 

---

### Verse 18 (Markende Puran 0.678)
- **Original**: गहीँ हो पाती है; अतः तपस्थिनि! दिनके ताशसे है। में जातती हूँ कि स्व्रियोंके लिये पतिके समान समस्त शुभ कर्मोक्ा नाश हो जायगा और उनके दूसरी कोई गति नड़ों है। गतिपमें किया हुआ प्रेम
- **Translation**: 

---

### Verse 19 (Markende Puran 0.679)
- **Original**: नाशसे चृष्टिम बाथा पड़नेके कारण इस संसारका इहलोक और परलोकर्ों भी उपकार करनेवाला
- **Translation**: 

---

### Verse 20 (Markende Puran 0.680)
- **Original**: ही उच्छेद हों जावगा। अत; यदि तुम इस होता है! यरशास्वरि! पत्िके प्रसादसे ही नारी इस जातृको आपत्तिसे बचाना चाहती हो तो लोक और परलोकमें भी सुख पाती है; क्योंकि
- **Translation**: 

---

