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

### Verse 1 (Bramha 0.2401)
- **Original**: राक्षसों और स्थावर भूतोंकी अपनी मायासे सृष्टि काम, क्रोध एवं द्वेषसे रहित, अनासक्ू, निष्पाप,
- **Translation**: 

---

### Verse 2 (Bramha 0.2402)
- **Original**: करके मैं पुनः: उनका संहार करता हूँ। फिर सत्त्वस्थ, अहंकारशून्य तथा अध्यात्मतत्त्वके ज्ञाता
- **Translation**: 

---

### Verse 3 (Bramha 0.2403)
- **Original**: कर्मकालमें उनके योग्य शरीरका विचार करके ब्राह्मण सदा मेरा ही चिन्तन करते हुए उपासना
- **Translation**: 

---

### Verse 4 (Bramha 0.2404)
- **Original**: सृष्टि करता हूँ। मेरा स्वरूपभूत धर्म सत्ययुगमें करते हैं। मैं ही संवर्तक ज्योति, मैं ही संवर्तक
- **Translation**: 

---

### Verse 5 (Bramha 0.2405)
- **Original**: श्वेत रहता है, त्रेतामें श्याम होता है, द्वापर आनेपर अग्रि, मैं ही संबर्तक सूर्य और मैं ही संवर्तक
- **Translation**: 

---

### Verse 6 (Bramha 0.2406)
- **Original**: लाल हो जाता है और कलियुगमें काला पड़ वायु हूँ। आकाशमें जो ये तारे दिखायी देते हैं, इन
- **Translation**: 

---

### Verse 7 (Bramha 0.2407)
- **Original**: जाता है। प्रलयकाल आनेपर मैं ही अत्यन्त दारुण सबको मेरे ही रोम-कूप समझो। रब्रोंसे भरे हुए
- **Translation**: 

---

### Verse 8 (Bramha 0.2408)
- **Original**: कालरूप हो अकेला ही समस्त त्रिलोकीका नाश समुद्र और चारों दिशाओंको मेरे ही स्वरूप जानो। , करता हूँ। उत्पत्ति, पालन और संहार-ये तीन मनुष्य जिस कर्मका अनुष्ठान करके कल्याणके
- **Translation**: 

---

### Verse 9 (Bramha 0.2409)
- **Original**: मेरे ही धर्म हैं। मैं सम्पूर्ण विश्वका आत्मा और * यदा यदा हि धर्मस्य ग्लानिर्धवति सत्तम
- **Translation**: 

---

### Verse 10 (Bramha 0.2410)
- **Original**: अध्युत्थानमधर्मस्य तदा53त्मार्न सृजाम्यहम्‌। (56। 35-36)
- **Translation**: 

---

### Verse 11 (Bramha 0.2411)
- **Original**: *मार्कण्डेय मुनिको प्रलयकालमें बालमुकुन्दका दर्शत और उनका वरदान प्राप्त होता «117 4 सुन नमय3 2075 >-छाछ 22% -ऋनचचछण 5: नाछ सब लोकॉंको सुख पहुँचानेवाला हूँ। मेरा किसीसे
- **Translation**: 

---

### Verse 12 (Bramha 0.2412)
- **Original**: ब्रह्माजी जागते नहीं तबतक तुम यहीं निर्भय पार्थक्य नहीं है। मैं सर्वव्यापी, अनन्त और
- **Translation**: 

---

### Verse 13 (Bramha 0.2413)
- **Original**: होकर सुखपूर्वक विचरो। उनके जागनेके बाद मै इन्द्रियॉंका नियन्ता हूँ। मेंरे डग बहुत बड़े हैं। मैं
- **Translation**: 

---

### Verse 14 (Bramha 0.2414)
- **Original**: अकेला ही समस्त भूतों और उनके शरीरोंकी अकेला हीं काल-चक्रका संचालन करता हूँ। जो
- **Translation**: 

---

### Verse 15 (Bramha 0.2415)
- **Original**: सृष्टि करूँगा।'” ब्रह्मका रूप है, वह मेरा ही है। वही सम्पूर्ण
- **Translation**: 

---

### Verse 16 (Bramha 0.2416)
- **Original**: इतना कहकर भगबानूने मुनिबर मार्कण्डेयजीसे भूतोंकों शान्ति देनेवाला है। ठसका उद्यम सम्पूर्ण पूछा-“मुने! तुमने जिस अभिप्रायसे मेरी स्तुति भूतोंके हितके लिये ही होता है। मुनिश्रेष्ठट इस
- **Translation**: 

---

### Verse 17 (Bramha 0.2417)
- **Original**: की है, उसे कहो। मैं तुफ्हें शीघ्र ही उत्तम वरदान प्रकार मेरा आत्मा सम्पूर्ण भूतोंमें संनिहित है।
- **Translation**: 

---

### Verse 18 (Bramha 0.2418)
- **Original**: दूँगा।! भगवानूका यह कल्याणमय वचन सुनकर फिर भी मुझे कोई नहीं जानता। भक्तमण सब
- **Translation**: 

---

### Verse 19 (Bramha 0.2419)
- **Original**: मार्कण्डेय मुनि सहसा उनके चरणोंमें गिर पड़े लोकॉमें सर्वथा मेरा पूजन करते हैं। ब्रह्मन्‌! मुझमें
- **Translation**: 

---

### Verse 20 (Bramha 0.2420)
- **Original**: और इस प्रकार बोले--'देवेश! मैंने आपके तुमने जो कुछ भी क्लेशका अनुभव किया है, वह
- **Translation**: 

---

