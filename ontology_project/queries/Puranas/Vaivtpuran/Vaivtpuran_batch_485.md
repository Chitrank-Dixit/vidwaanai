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

### Verse 1 (Vaivtpuran 27.7168)
- **Original**: पृथ्वीके अंशको पृथ्वी, जलांशकों जल, शून्यांशको और संकेतपूर्वक नाम--ये प्रातःकालके स्वप्रसदूश
- **Translation**: 

---

### Verse 2 (Vaivtpuran 27.7169)
- **Original**: आकाश, वायुके अंशको वायु तथा तेजांशको निरर्थक हैं। परमात्माके अंशभूत आत्माके चले
- **Translation**: 

---

### Verse 3 (Vaivtpuran 27.7170)
- **Original**: तेज ग्रहण कर लेता है। इस प्रकार सभी अंश जानेपर भूख, निद्रा, दया, शान्ति, क्षमा, कान्ति, अपने-अपने अंशीमें विलीन हो जाते हैं; फिर प्राण, मन तथा ज्ञान सभी चले जाते हैं। जैसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 27.7171)
- **Original**: रोनेसे कौन वापस आयेगा। मरनेके बाद तो राजाधिराजके पीछे नौकर-चाकर चलते हैं, उसी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 27.7172)
- **Original**: नाम, शास्त्र, ज्ञाना, यश और कर्मकी कथामात्र प्रकार बुद्धि तथा सारी शक्तियाँ उसीका अनुगमन
- **Translation**: 

---

### Verse 6 (Vaivtpuran 27.7173)
- **Original**: अवशिष्ट रह जाती है। इसलिये जो वेदविहित करती हैं; अत: तुम यत्रपूर्वक श्रीकृष्णणा भजन
- **Translation**: 

---

### Verse 7 (Vaivtpuran 27.7174)
- **Original**: पारलौकिक कर्म है, इस समय तुम बही करो; करो। बेटा! कौन किसके पितर हैं और कौन
- **Translation**: 

---

### Verse 8 (Vaivtpuran 27.7175)
- **Original**: क्योंकि जो परलोकके लिये हितकारी हो, वही किसके पुत्र हैं। ये सभी इस दुस्तर भवसागरमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 27.7176)
- **Original**: वास्तवमें पुत्र है और वही बन्धु है। भृगुके उस कर्मरूपी लहरियोंसे प्रेरित हो रहे हैं। पुत्र!
- **Translation**: 

---

### Verse 10 (Vaivtpuran 27.7177)
- **Original**: वचनको सुनकर महासाध्वी रेणुकाने उसी क्षण ज्ञानीलोग विलाप नहीं करते, अत: अब तुम भी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 27.7178)
- **Original**: शोकका परित्याग कर दिया और मुनिसे कहना रुदन मत करो; क्योंकि रोनेके कारण आँसुओंके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 27.7179)
- **Original**: आरम्भ किया। (अध्याय 27) #+4-+--स्य#प482तजरज रेणुका-भृगु-संबाद, रेणुकाका पतिके साथ सती होना, परशुरामका पिताकी अन्त्येष्टि क्रिया करके ब्रह्मके पार्स जाना और अपनी प्रतिज्ञा सुनाना, ब्रह्माका उन्हें शिवजीके पास भेजना रेणुकाने पूछा-ब्रह्मन्‌! अब मैं अपने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 27.7180)
- **Original**: पुण्यात्मा पतिका अनुगमन करो; क्योंकि ऋतुका प्राणनाथका अनुगमन करना चाहती हूँ। दूसरोंको
- **Translation**: 

---

### Verse 14 (Vaivtpuran 27.7181)
- **Original**: चौथा दिन पतिके सभी कार्योंमें शुद्ध माना जाता मान देनेवाले ये मेंरे पतिदेव आज मेरे ऋतुकालके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 27.7182)
- **Original**: है। जो भक्तिदाता है, वही पुत्र है; जो अनुगमन चौथे दिन मृत्युको प्राप्त हुए हैं; अतः वेदवेत्ताओँमें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 27.7183)
- **Original**: करती है, वही स्त्री है; जो दान देता है, वही बन्धु श्रेष्ठ मुने! बतलाइये, अब इस विषयमें कैसी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 27.7184)
- **Original**: है; जो गुरुकी अर्चना करता है, वही शिष्य है; व्यवस्था करनी चाहिये। मेरे कई जन्मोंका पुण्य
- **Translation**: 

---

### Verse 18 (Vaivtpuran 27.7185)
- **Original**: जो रक्षा करे, वही अभीष्ट देवता है; जो प्रजाका उदय हुआ है, जिसके फलस्वरूप आप सहसा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 27.7186)
- **Original**: पालन करे, वही राजा है; जो अपनी पत्नीकी उपस्थित हुए. हैं।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 27.7187)
- **Original**: बुद्धिको धर्ममें नियोजित करता है, वही स्वामी भूगुने कहा--अहो महासति! तुम अपने । है; जो धर्मोपदेशक तथा हरिभक्ति प्रदान करनेवाला * ज्ञातिनों मा रुवन्त्येब मा रोदी: पुत्र साम्प्रतम्‌ । रोदनाश्रुप्रपतनान्मृतानां. नरक॑ धुवम्‌
- **Translation**: 

---

