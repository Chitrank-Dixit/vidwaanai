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

### Verse 1 (Vishnu Puran 0.9661)
- **Original**: 49 8 फ ख ल्‍लए भीविष्णुपुराण _ऋअआ* 10 [ अब 10 (इच्छानुसार रूप घारण करनेवाले) हैं। वे मनोब्राज्छित रूप धारण वरके अपने-अपने शिख्रोंपर विहार किया करते हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9662)
- **Original**: जब कभी वनसासीगण इन गिरिदेवॉको किसी तरहकी बाधा पहुँचाते हैं तो वे सिंहादि रूप धारणकर उन्हें मार डालते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9663)
- **Original**: 35 । अतः आजसे [ इस इन्द्रयज्ञके स्थानमें गिर्यिज्ञ अथवा गोयइ्का प्रचार होना चाहिये। हमें हन्द्रसे क्या प्रयोजन है? हमारे देवता तो गौएँ और पर्वत ही हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9664)
- **Original**: ब्राह्मणट्ओोग मन्न-यज्ञ तथा कृषकगण सौरयज्ञ (हलका पूजन) करते हैं, अतः पर्वत और बनोंमें रहनेवाले हमलोगोंको गिरियज्ञ और गोयज्ञ करने चाहिये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9665)
- **Original**: “अतएव आपल्ोग विधिपूर्वक मेध्य पशुओंकी बलि देकर विधिध सामग्रियोंसे गोवर्धनपर्वतकी पूजा करें
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9666)
- **Original**: 38 । आज सम्पूर्ण व्रजका दूध एकत्रित कर लो और उससे ब्राह्मणों तथा अन्यान्य याचक्रोंम्ले भोजन कराओ; इस विषयमें और अधिक सोय-बियार मत करो
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9667)
- **Original**: गोवर्धनकी पूजा, होम और ब्राह्मण-भोजन समाप्त होनेपर दरद-ऋतुके पुष्पोंसे सजे हुए मस्तकवाली गौएँ गिरिराजकी प्रदक्षिणा करें
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9668)
- **Original**: हैं गोपगण ! आपलोग यदि प्रीतिपूर्वक मेरी इस सम्मतिके अनुसार कार्य करेंगे तो इससे गौओंको, गिरिणज और मुझको अह्क्त प्रसन्नता होगी”
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9669)
- **Original**: श्रीपराशस्जी खोले--फृष्णवन्द्रके इन वाक्योंको सुनकर नन्‍्द आदि व्रजबासी गोपनि प्रसप्नतासे खिल्े हुए मुखसे 'साधु, साथु' कहा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9670)
- **Original**: और बोले--हे वत्स ! तुमने अपना जो बिचार प्रकट किया है वह बड़ा हो सुन्दर है; हम सब ऐसा हो करेंगे; आज गिरियज्ञ किया जाय
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9671)
- **Original**: तदनन्तर उन त्रजवासियोंने गिरियज्ञका अनुष्ठान किया तंथा दही, खीर और मांस आदिसे पर्वतराजकों बलि दी
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9672)
- **Original**: सैकड़ों, हजाएों ब्राहणोंकों भोजन कगया तथा पष्पार्थित गौओं और सजल जलघस्के समान गजनिवाले साड़ोंन गोबर्धनकी परिक्रमा की
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9673)
- **Original**: हे द्विज ! उस समय कृष्णयच्ने पर्वतके शिसरपर अन्यरूपसे प्रकट होकर
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9674)
- **Original**: यह दिखल्ाते हुए कि मैं मूर्तिमान्‌ गिरिराज हूँ, उन गोपश्रेष्ठोकि चढ़ाये हुए विविध व्यञनोंकों ग्रहण किया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9675)
- **Original**: कृष्णचद्धने अपने निजरूपसे गोपोंके साथ पर्वतराजके दिखरपर चढ़कर अपने हो दूसरे स्वरूपका पूजन किया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9676)
- **Original**: तदनन्तर उनके अन्तर्धान होनेपर गोपगण अपने अभीष्ट वर पाकर गिरियज्ञ समाप्त करके फिर अपने- अपने गोष्ठोंमें चफ़े आये
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9677)
- **Original**: मा इति श्रीविष्णुपुराणे पंकज टशमो5श्याय:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9678)
- **Original**: श्र पश्नचम अंश ग्यारहवाँ अध्याय इच्रका कोप और श्रीकृष्णका गोखर्धन-धारण औपदशर उवाच मस्त प्रतिहते शक्रो मैत्रेयातिरुषान्लितः । संबर्तक॑ नाप गणं तोयदानामथात्रवीत्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9679)
- **Original**: 9 भो भो मेघा निशम्यैत्तहलन गदतो. मम । आज्ञानन्तरमेवाशु क्रियतामविच्चारितम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9680)
- **Original**: 2 नन्दगोपस्मुदुर्बुद्धिगोपैरन्यैस्सहायवान्‌ू._। कृष्णाश्रयबलाध्मातों मखभड्रमचीकरत्‌
- **Translation**: 

---

