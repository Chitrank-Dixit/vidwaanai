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

### Verse 1 (Vaivtpuran 543.13694)
- **Original**: देबता और मुनि भी रो पड़े। फिर बे मानसशायी धर्मने कहा--प्रमथेश्व! आपका कल्याण
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13695)
- **Original**: देवता शीघ्र ही कैलासपर्बतकों चल दिये तथा हो। उठिये, उठिये और श्रीहरिका स्मरण करते
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13696)
- **Original**: दो ही घड़ीमें शिवके निवासस्थानपर सानन्द जा हुए माहेन्द्र-योगमें पार्वतीके साथ यात्रा कीजिये। पहुँचे। यह देखकर वहाँके मड्जल-कृत्यका वृन्दावन-विनोदिनि! धर्मकी बात सुनकर सम्पादन करनेके लिये देवताओं और मुनियोंकी शंकरने पार्वतीके साथ माहेद्ध-योगमें यात्रा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13697)
- **Original**: पत्रियाँ भी दीप लिये शौघ्रतापूर्वक सहर्ष वहाँ आरम्भ की। पार्वतीके साथ देवेश्वर शंकरके यात्रा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13698)
- **Original**: आ गयीं। वायु, कुबेर और शुक्रकी स्त्रियाँ, करते समय मेना उच्चस्वरसे रो पड़ीं और उन बृहस्पतिकी पत्नी तारा, दुर्वासाकी स्त्री, अत्रि- कृपानिधानसे बोलीं। भार्या अनसूया, चन्द्रमाकी पत्रियाँ, देवकन्या, मेनाने कहा--कृपानिधे ! कृपा करके मेरी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13699)
- **Original**: नागकन्या तथा सहस्रों मुनिकन्याएँ वहाँ उपस्थित बच्चीका पालन कीजियेगा। आप आशुतोष हैं।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13700)
- **Original**: हुईं। वहाँ जिन असंख्य कामिनियोंका समूह आया इसके सहसौरों दोषोंकों क्षमा कीजियेगा। मेरी बेटी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13701)
- **Original**: था, उन सबकी गणना करनेमें कौन समर्थ है? जन्म-जन्ममें आपके चरणकमलॉमें अनन्यभक्ति
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13702)
- **Original**: उन सबने मिलकर नवदम्पतिका उनके निवास- रखती आयी है। सोते-जागते हर समय इसे अपने
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13703)
- **Original**: मन्दिरमें प्रवेश कराया तथा उन महे ध्वरको रमणीय स्वामी महादेवके सिवा दूसरे किसीकी याद नहीं
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13704)
- **Original**: रत्रमय सिंहासनपर बिठाया। वहाँ भगवान्‌ शिवने आती है। आपके प्रति भक्तिकी बातें सुनते ही
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13705)
- **Original**: सतौकों उनका पहलेवाला घर दिखाया और इसका अड्भ-अड्र पुलकित हो उठता है और
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13706)
- **Original**: प्रसन्नतापूर्वक पूछा--' प्रिये! क्‍या तुम्हें अपने इस नेत्रोंसे आनन्दके आँसू बहने लगते हैं। मृत्युझ्य !
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13707)
- **Original**: घरकी याद आती है? यहींसे तुम अपने पिताके आपको निन्दा कानमें पड़नेपर यह ऐसी मौन । निवास-स्थानकों गयी थीं। अन्तर इतना ही है हो जाती है, मानो मर गयी हो। कि इस समय तुम गिरिराजकुमारी हो और उस मेना यह कह ही रही थी कि हिमवान्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13708)
- **Original**: समय यहाँ दक्षकन्याके रूपमें निवास करती थीं। तत्काल वहाँ आ पहुँचे और अपनी बच्चीको
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13709)
- **Original**: तुम्हें पूर्वजन्मकी बातोंका सदा स्मरण रहता है; छातीसे लगा फूट-फूटकर रोने लगे--वत्से !
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13710)
- **Original**: इसीलिये पिछली बातोंकी याद दिला रहा हूँ। हिमालयको--मेंरे इस घरको सूना करके तू कहाँ
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13711)
- **Original**: यदि तुम्हें उन बातोंका स्मरण है तो कहो।' चली जा रही है? तेरे गुणोंको याद करके मेरा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13712)
- **Original**: भगवान्‌ शंकरकी बात सुनकर पार्वती हृदय अवश्य ही विदीर्ण हो जायगा।' यों कहकर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13713)
- **Original**: मुस्करायीं और बोलीं--'प्राणनाथ! मुझे सब शैलराजने अपनी शिवा शिवको सौंप दी और
- **Translation**: 

---

